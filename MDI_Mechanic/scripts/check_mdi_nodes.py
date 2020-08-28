import os
import subprocess
import sys
import yaml
from graphviz import Digraph

# Path to this file
file_path = os.path.dirname(os.path.realpath(__file__))

# Path to the top-level directory
base_path = file_path + "/../.."

# Platform-specific hostname
if sys.platform == "darwin":
    hostname = "host.docker.internal"
else:
    hostname = "localhost"




# Paths to enter each identified node
node_paths = { "@DEFAULT": "" }

# Paths associated with the edges for the node graph
node_edge_paths = [ ("@DEFAULT", "") ]

def format_return(input_string):
    my_string = input_string.decode('utf-8')

    # remove any \r special characters, which sometimes are added on Windows
    my_string = my_string.replace('\r','')

    return my_string

def insert_list( original_list, insert_list, pos ):
    for ielement in range(len(insert_list)):
        element = insert_list[ielement]
        original_list.insert( pos + ielement + 1, element )

n_tested_commands = 0
def test_command( command, nrecv, recv_type, nsend, send_type ):
    global n_tested_commands
    global base_path
    global hostname
    #print("Starting min_driver.py with command: " + str(command))
    
    # Remove any leftover files from previous runs of min_driver.py
    #os.system("rm ./drivers/min_driver.dat")
    #os.system("rm ./drivers/min_driver.err")
    if os.path.exists("./drivers/min_driver.dat"):
        os.remove("./drivers/min_driver.dat")
    if os.path.exists("./drivers/min_driver.err"):
        os.remove("./drivers/min_driver.err")

    port_num = 9050 + n_tested_commands
    mdi_driver_options = "-role DRIVER -name driver -method TCP -port " + str(port_num)
    #print("   Driver Options: " + str(command) + " " + str(nrecv) + " " + str(recv_type) + " " + str(nsend) + " " + str(send_type))
    if nrecv is not None and nsend is not None:
       driver_proc = subprocess.Popen([sys.executable, "min_driver.py", "-command", command, 
                                        "-nreceive", str(nrecv), "-rtype", str(recv_type), 
                                        "-nsend", str(nsend), "-stype", str(send_type), 
                                        "-mdi", mdi_driver_options],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd="./drivers")
    elif nrecv is not None:
        driver_proc = subprocess.Popen([sys.executable, "min_driver.py", "-command", command, 
                                        "-nreceive", str(nrecv), "-rtype", str(recv_type), 
                                        "-mdi", mdi_driver_options],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd="./drivers")
    elif nsend is not None:
        driver_proc = subprocess.Popen([sys.executable, "min_driver.py", "-command", command, 
                                        "-nsend", str(nsend), "-stype", str(send_type), 
                                        "-mdi", mdi_driver_options],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd="./drivers")
    else:
        driver_proc = subprocess.Popen([sys.executable, "min_driver.py", "-command", command, 
                                        "-mdi", mdi_driver_options],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd="./drivers")
    
    # Run the engine, using Docker
    mdi_engine_options = "-role ENGINE -name TESTCODE -method TCP -hostname " + str(hostname) + " -port " + str(port_num)
    working_dir = str(base_path) + "/user/mdi_tests/test1"
    os.system("rm -rf " + str(base_path) + "/user/mdi_tests/.work")
    os.system("cp -r " + str(working_dir) + " " + str(base_path) + "/user/mdi_tests/.work")
    docker_string = "docker run --net=host --rm -v " + str(base_path) + ":/repo -it travis/mdi_test bash -c \"cd /repo/user/mdi_tests/.work && export MDI_OPTIONS=\'" + str(mdi_engine_options) + "\' && ./run.sh\""
    os.system(docker_string)

    # Convert the driver's output into a string
    driver_tup = driver_proc.communicate()
    driver_out = format_return(driver_tup[0])
    driver_err = format_return(driver_tup[1])
    
    #print("   Driver out: " + str(driver_out))
    #print("   Driver err: " + str(driver_err))

    n_tested_commands += 1
    if driver_err == "":
        print("WORKED")
        return True
    else:
        print("FAILED")
        return False

def find_nodes():
    global node_paths
    global node_edge_paths
    
    # List of all node commands in the MDI Standard
    command_list = []
    commands = None
    
    with open(r'../mdi_standard.yaml') as standard_file:
        standard = yaml.load(standard_file, Loader=yaml.FullLoader)
        commands = standard['commands']
        
        for command in commands.keys():
            if command[0] == '@' and command != '@':
                command_list.append( command )

    # Check which of the MDI Standard commands work from the @DEFAULT node
    for command in command_list:
        command_works = test_command( command, None, None, None, None )
        if command_works:
            #print("Working command: " + str(command))
            node_paths[command] = command
            node_edge_paths.append( (command, command) )
    
    # From the nodes that have currently been identified, attempt to use the "@" command to identify more nodes
    original_nodes = []
    for node in node_paths.keys():
        original_nodes.append(node)
    for node in original_nodes:
        for ii in range(20):
            new_path = node_paths[node]
            for jj in range(ii+1):
                new_path += " @"
            command = new_path + " <@"
            print("CCC Node path test: " + str(command))
            command_works = test_command( command, "MDI_COMMAND_LENGTH", "MDI_CHAR", None, None )
            print("Working path: " + str(command))
        
            # Read the name of the node
            node_name = None
            if os.path.isfile("./drivers/min_driver.dat"):
                with open("./drivers/min_driver.dat", "r") as f:
                    node_name = f.read()
            print("DDD Name of new node: " + str(node_name))
            err_value = None
            if os.path.isfile("./drivers/min_driver.err"):
                with open("./drivers/min_driver.err", "r") as f:
                    err_value = f.read()
            if err_value == "0":
                print("EEE: Worked")
                
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
    
    print("AAA: " + str(command_list))
    print("BBB: " + str(node_paths))

def write_supported_commands():
    global node_paths
    
    # List of all commands in the MDI Standard
    command_list = []
    commands = None
    
    with open(r'../mdi_standard.yaml') as standard_file:
        standard = yaml.load(standard_file, Loader=yaml.FullLoader)
        commands = standard['commands']
    
        for command in commands.keys():
            values = commands[command]
            command_list.append( command )

    # Identify all supported nodes, and find a path to them
    find_nodes()
    
    # Write the README.md section that lists all supported commands
    command_sec = []

    # Write the section header
    command_sec.append( "## Supported Commands\n" )
    command_sec.append( "\n" )
    header_line = "| "
    for node in node_paths.keys():
        header_line += "| " + str(node) + " "
    header_line += "|\n"
    command_sec.append( header_line )
    header_line = "| ------------- "
    for node in node_paths.keys():
        header_line += "| ------------- "
    header_line += "|\n"
    command_sec.append( header_line )

    # Write the list of supported commands
    for command in command_list:
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
        for node in node_paths.keys():
            command_with_path = node_paths[node] + " " + command
            #print("FFF: " + str(command_with_path), end=" ")
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

    dot = Digraph(comment='Node Report', format='svg')
    #dot.node('@DEFAULT', '@DEFAULT')
    #dot.node('@INIT_MD', '@INIT_MD')
    #dot.node('@INIT_OPTG', '@INIT_OPTG')
    #dot.node('@INIT_MC', '@INIT_MC')
    #dot.node('@INIT_MD_', '@PRE-FORCES\n@FORCES\n@COORDS')
    #dot.node('@INIT_OPTG_', '@PRE-FORCES\n@FORCES\n@COORDS')

    #dot.edge('@DEFAULT', '@INIT_MD')
    #dot.edge('@DEFAULT', '@INIT_OPTG')
    #dot.edge('@DEFAULT', '@INIT_MC')
    #dot.edge('@INIT_MD', '@INIT_MD_')
    #dot.edge('@INIT_OPTG', '@INIT_OPTG_')

    print("*********************************************")
    print("* Creating node graph                       *")
    print("*********************************************")

    print("node_edge_paths: " + str(node_edge_paths))

    #for node_name in node_paths.keys():
    #    dot.node( node_name, node_name )

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

    for node in nodes.keys():
        dot.node( node, nodes[ node ], shape='box' )

    for edge in edges:
        dot.edge( edge[0], edge[1] )
    
    #for edge_path in node_edge_paths:
    #    print("edge_path: " + str(edge_path))
    #    name = edge_path[0]
    #    path = edge_path[1]
    #    dot.node( name, name )

    #    # Add edges for the nodes that are directly accessed from @DEFAULT
    #    if name == path:
    #        dot.edge('@DEFAULT', name)
    #    elif path.find(' @ ') != -1 or path[-2:] == ' @':
    #        split_path = path.split()
    #        parent = split_path[0]
    #        dot.edge(parent, name)

    dot.render(str(base_path) + '/report/graphs/node-report.gv')
    
# Read the README.md file
with open(r'../README.base') as file:
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
tempfile = str(base_path) + '/MDI_Mechanic/.temp/README.temp'
os.makedirs(os.path.dirname(tempfile), exist_ok=True)
with open(tempfile, 'w') as file:
    file.writelines( readme )

# Create the node graph
node_graph()
