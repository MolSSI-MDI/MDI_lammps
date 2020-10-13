import os
import pickle
import subprocess

def get_base_path():
    # Get the base directory
    file_path = os.path.dirname(os.path.realpath(__file__))
    base_path = os.path.dirname( os.path.dirname( os.path.dirname( file_path ) ) )
    return base_path

def get_compose_path( method ):
    base_path = get_base_path()
    compose_path = os.path.join( base_path, "MDI_Mechanic", "docker", method )
    return compose_path

def format_return(input_string):
    my_string = input_string.decode('utf-8')

    # remove any \r special characters, which sometimes are added on Windows
    my_string = my_string.replace('\r','')

    return my_string

def insert_list( original_list, insert_list, pos ):
    for ielement in range(len(insert_list)):
        element = insert_list[ielement]
        original_list.insert( pos + ielement + 1, element )

def docker_error( docker_tup, error_message ):
    docker_out = format_return(docker_tup[0])
    docker_err = format_return(docker_tup[1])
    print("-------- BEGIN DOCKER OUTPUT --------")
    print( str(docker_out) )
    print("-------- END DOCKER OUTPUT ----------")
    print("-------- BEGIN DOCKER ERROR ---------")
    print( str(docker_err) )
    print("-------- END DOCKER ERROR -----------")
    raise Exception(error_message)

def get_mdi_standard():
    # Path to the file where the standard will be written
    base_path = get_base_path()
    standard_file = os.path.join( base_path, "MDI_Mechanic", ".temp", "standard.pickle" )
    
    parse_proc = subprocess.Popen( ["docker", "run", "--rm",
                                   "-v", str(base_path) + ":/repo",
                                   "-it", "mdi_mechanic/mdi_mechanic",
                                   "bash", "-c",
                                   "cd /repo/MDI_Mechanic/scripts/utils && python parse_standard.py"],
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    parse_tup = parse_proc.communicate()
    if parse_proc.returncode != 0:
        docker_error( parse_tup, "Parse process returned an error." )

    with open(standard_file, 'rb') as handle:
        standard = pickle.load(handle)
    return standard
