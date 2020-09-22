import os
import subprocess
import pickle
from .utils import get_base_path, format_return, insert_list, docker_error, get_mdi_standard

# Paths to enter each identified node
node_paths = { "@DEFAULT": "" }

# Paths associated with the edges for the node graph
node_edge_paths = [ ("@DEFAULT", "") ]

def test_command( command, nrecv, recv_type, nsend, send_type ):
    # Remove any leftover files from previous runs of min_driver.py
    base_path = get_base_path()
    dat_file = os.path.join( base_path, "MDI_Mechanic", "scripts", "drivers", "min_driver.dat" )
    err_file = os.path.join( base_path, "MDI_Mechanic", "scripts", "drivers", "min_driver.err" )
    if os.path.exists( dat_file ):
        os.remove( dat_file )
    if os.path.exists( err_file ):
        os.remove( err_file )

    mdi_driver_options = "-role DRIVER -name driver -method TCP -port 8021"

    # Create the docker script
    docker_file = str(base_path) + '/MDI_Mechanic/.temp/docker_mdi_mechanic.sh'
    docker_lines = [ "#!/bin/bash\n",
                     "\n",
                     "# Exit if any command fails\n",
                     "\n",
                     "cd MDI_Mechanic/scripts/drivers\n",
                     "python min_driver.py \\\n"
    ]
    if command is not None:
        docker_lines.append( "   -command \'" + str(command) + "\' \\\n" )
    if nrecv is not None:
        docker_lines.append( "   -nreceive \'" + str(nrecv) + "\' \\\n" )
    if recv_type is not None:
        docker_lines.append( "   -rtype \'" + str(recv_type) + "\' \\\n" )
    if nsend is not None:
        docker_lines.append( "   -nsend \'" + str(nsend) + "\' \\\n" )
    if send_type is not None:
        docker_lines.append( "   -stype \'" + str(send_type) + "\' \\\n" )
    docker_lines.append( "   -mdi \"" + str(mdi_driver_options) + "\"\n" )
    os.makedirs(os.path.dirname(docker_file), exist_ok=True)
    with open(docker_file, 'w') as file:
        file.writelines( docker_lines )

    docker_path = os.path.join( base_path, "MDI_Mechanic", "docker" )

    # Run "docker-compose up"
    up_proc = subprocess.Popen( ["docker-compose", "up", "--exit-code-from", "mdi_mechanic", "--abort-on-container-exit"],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                cwd=docker_path )
    up_tup = up_proc.communicate()
    up_out = format_return(up_tup[0])
    up_err = format_return(up_tup[1])
    if up_proc.returncode != 0:
        print("FAILED", flush=True)
        return False

    # Run "docker-compose down"
    down_proc = subprocess.Popen( ["docker-compose", "down"],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                cwd=docker_path )
    down_tup = down_proc.communicate()
    down_out = format_return(down_tup[0])
    down_err = format_return(down_tup[1])
    if down_proc.returncode != 0:
        print("FAILED", flush=True)
        return False


    print("WORKED", flush=True)
    return True

def find_nodes():
    global node_paths
    global node_edge_paths
    
    # List of all node commands in the MDI Standard
    command_list = []
    commands = None
    
    base_path = get_base_path()
    standard = get_mdi_standard()
    commands = standard['commands']
    
    for command in commands:
        if command[0] == '@' and command != '@':
            command_list.append( command )
    ordered_commands = sorted( command_list )

    # Check which of the MDI Standard commands work from the @DEFAULT node
    for command in ordered_commands:
        command_works = test_command( command, None, None, None, None )
        if command_works:
            node_paths[command] = command
            node_edge_paths.append( (command, command) )
    
    # From the nodes that have currently been identified, attempt to use the "@" command to identify more nodes
    print("Searching for supported nodes", flush=True)
    original_nodes = []
    for node in node_paths.keys():
        original_nodes.append(node)
    ordered_nodes = sorted( original_nodes )
    for node in ordered_nodes:
        for ii in range(20):
            new_path = node_paths[node]
            for jj in range(ii+1):
                new_path += " @"
            command = new_path + " <@"
            print("Checking for node at: " + str(new_path), end=" ")
            command_works = test_command( command, "MDI_COMMAND_LENGTH", "MDI_CHAR", None, None )
        
            # Read the name of the node
            node_name = None
            dat_file = os.path.join( base_path, "MDI_Mechanic", "scripts", "drivers", "min_driver.dat" )
            err_file = os.path.join( base_path, "MDI_Mechanic", "scripts", "drivers", "min_driver.err" )
            if os.path.isfile( dat_file ):
                with open( dat_file, "r") as f:
                    node_name = f.read()
            err_value = None
            if os.path.isfile( err_file ):
                with open( err_file, "r") as f:
                    err_value = f.read()
                
            if node_name is not None and not node_name in node_paths.keys():
                node_paths[node_name] = new_path

            # Check whether this should be added to the node graph
            if node_name is not None:
                split_path = new_path.split()
                include = True
                for node_edge in node_edge_paths:
                    if node_edge[0] == node_name:
                        path = node_edge[1].split()
                        if path[0] == split_path[0]:
                            include = False

                if include:
                    node_edge_paths.append( (node_name, new_path) )

    print("Completed search for nodes.", flush=True)
    print("Found the following nodes: " + str(node_paths.keys()) )

def write_supported_commands():
    global node_paths
    
    # List of all commands in the MDI Standard
    command_list = []
    commands = None
    
    base_path = get_base_path()
    standard = get_mdi_standard()
    commands = standard['commands']
    
    for command in commands.keys():
        values = commands[command]
        command_list.append( command )
    ordered_commands = sorted( command_list )

    # Identify all supported nodes, and find a path to them
    find_nodes()
    ordered_nodes = sorted( node_paths.keys() )
    
    # Write the README.md section that lists all supported commands
    command_sec = []

    # Write the section header
    command_sec.append( "## Supported Commands\n" )
    command_sec.append( "\n" )
    header_line = "| "
    for node in ordered_nodes:
        header_line += "| " + str(node) + " "
    header_line += "|\n"
    command_sec.append( header_line )
    header_line = "| ------------- "
    for node in ordered_nodes:
        header_line += "| ------------- "
    header_line += "|\n"
    command_sec.append( header_line )

    # Write the list of supported commands
    for command in ordered_commands:
        nrecv = None
        recv_type = None
        nsend = None
        send_type = None
        print("---------------------------------------")
        print("Testing command: " + str(command))
        if commands[command] is not None and 'recv' in commands[command].keys():
            nrecv = commands[command]['recv']['count']
            recv_type = commands[command]['recv']['datatype']
        if commands[command] is not None and 'send' in commands[command].keys():
            nsend = commands[command]['send']['count']
            send_type = commands[command]['send']['datatype']
        
        line = "| " + str(command) + " "
        for node in ordered_nodes:
            command_with_path = node_paths[node] + " " + command
            padded_string = str(node).ljust(20, '.')
            print(padded_string, end=" ")
            command_works = test_command( command_with_path, nrecv, recv_type, nsend, send_type )
        
            if command_works:
                # Display a bright green box
                command_status = "![command](report/badges/box-brightgreen.svg)"
            else:
                # Display a light gray box
                command_status = "![command](report/badges/box-lightgray.svg)"

            line += "| " + str(command_status) + " "
        line += "|\n"
        command_sec.append( line )

    # Replace all ">" or "<" symbols with Markdown escape sequences
    for iline in range(len(command_sec)):
        line = command_sec[iline]
        line = line.replace(">", "&gt;")
        line = line.replace("<", "&lt;")
        command_sec[iline] = line
    
    return command_sec

def node_graph():
    global node_edge_paths

    print("*********************************************")
    print("* Creating node graph                       *")
    print("*********************************************")

    print("node_edge_paths: " + str(node_edge_paths))

    base_path = get_base_path()

    nodes = {}
    edges = []
    for edge_path in node_edge_paths:
        name = edge_path[0]
        path = edge_path[1].split()
        if '@' in path:
            parent_cluster = str(path[0]) + '_'
            if not parent_cluster in nodes.keys():
                nodes[ parent_cluster ] = str(name)
                edges.append( ( path[0], parent_cluster ) )
            else:
                nodes[ parent_cluster ] += '\n' + str(name)
        else:
            nodes[ name ] = name
            if name != '@DEFAULT':
                edges.append( ( '@DEFAULT', name ) )
    print("nodes: " + str(nodes))

    # Save the graph data to a file
    graph_data = { 'nodes': nodes,
                   'edges': edges }
    graph_file = os.path.join( base_path, "MDI_Mechanic", ".temp", "graph.pickle")
    os.makedirs(os.path.dirname(graph_file), exist_ok=True)
    with open(graph_file, 'wb') as handle:
        pickle.dump(graph_data, handle, protocol=min(pickle.HIGHEST_PROTOCOL, 4))

    # Render the graph within a docker image, so that it is consistent across machines
    graph_proc = subprocess.Popen( ["docker", "run", "--rm",
                                   "-v", str(base_path) + ":/repo",
                                   "-it", "mdi_mechanic/mdi_mechanic",
                                   "bash", "-c",
                                   "cd /repo/MDI_Mechanic/scripts/utils && python graph.py"],
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    graph_tup = graph_proc.communicate()
    if graph_proc.returncode != 0:
        docker_error( graph_tup, "Graph process returned an error." )

def analyze_nodes():
    base_path = get_base_path()

    # Read the README.md file
    readme_path = os.path.join(base_path,"MDI_Mechanic","README.base")
    with open(readme_path, "r") as file:
        readme = file.readlines()

    # Check the README.md file for any comments for travis
    for iline in range(len(readme)):
        line = readme[iline]
        sline = line.split()
        if len(sline) > 0 and sline[0] == '[travis]:':
            instruction = sline[3]

            if instruction == "supported_commands":
                # Need to insert a list of supported commands here
                command_sec = write_supported_commands()
                insert_list( readme, command_sec, iline )

    # Write the updates to the README file
    temp_file = os.path.join( base_path, 'MDI_Mechanic', '.temp', 'README.temp')
    os.makedirs(os.path.dirname(temp_file), exist_ok=True)
    with open(temp_file, 'w') as file:
        file.writelines( readme )

    # Create the node graph
    node_graph()
