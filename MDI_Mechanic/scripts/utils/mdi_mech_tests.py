import os
import subprocess

def format_return(input_string):
    my_string = input_string.decode('utf-8')

    # remove any \r special characters, which sometimes are added on Windows
    my_string = my_string.replace('\r','')

    return my_string

def test_validate():
    # Get the base directory
    file_path = os.path.dirname(os.path.realpath(__file__))
    base_path = os.path.dirname( os.path.dirname( os.path.dirname( file_path ) ) )

    # Run the engine test script
    bash_command = "docker run --net=host --rm -v " + str(base_path) + ":/repo -it travis/mdi_test bash -c \"cd /repo/user && ./validate_build.sh\""
    ret = os.system(bash_command)
    if ret != 0:
        raise Exception("Build validation script returned non-zero value.")

def test_engine():
    # Get the base directory
    file_path = os.path.dirname(os.path.realpath(__file__))
    base_path = os.path.dirname( os.path.dirname( os.path.dirname( file_path ) ) )

    # Run the engine test script
    working_dir = str(base_path) + "/user/engine_tests/test1"
    os.system("rm -rf " + str(base_path) + "/user/engine_tests/.work")
    os.system("cp -r " + str(working_dir) + " " + str(base_path) + "/user/engine_tests/.work")
    bash_command = "docker run --net=host --rm -v " + str(base_path) + ":/repo -it travis/mdi_test bash -c \"cd /repo/user/engine_tests/.work && ./run.sh\""
    ret = os.system(bash_command)
    if ret != 0:
        raise Exception("Engine test script returned non-zero value.")

def test_min():
    # Get the base directory
    file_path = os.path.dirname(os.path.realpath(__file__))
    base_path = os.path.dirname( os.path.dirname( os.path.dirname( file_path ) ) )
    docker_path = os.path.join( base_path, "MDI_Mechanic", "docker" )

    docker_file = str(base_path) + '/MDI_Mechanic/.temp/docker_mdi_mechanic.sh'
    docker_lines = [ "#!/bin/bash\n",
                     "\n",
                     "# Exit if any command fails\n",
                     "\n",
                     "cd MDI_Mechanic/scripts/drivers\n",
                     "python min_driver.py -command \'<NAME\' -nreceive \'MDI_NAME_LENGTH\' -rtype \'MDI_CHAR\' -mdi \'-role DRIVER -name driver -method TCP -port 8021\'\n"]
    os.makedirs(os.path.dirname(docker_file), exist_ok=True)
    with open(docker_file, 'w') as file:
        file.writelines( docker_lines )

    working_dir = str(base_path) + "/user/mdi_tests/test1"
    os.system("rm -rf " + str(base_path) + "/user/mdi_tests/.work")
    os.system("cp -r " + str(working_dir) + " " + str(base_path) + "/user/mdi_tests/.work")

    # Run "docker-compose up"
    up_proc = subprocess.Popen( ["docker-compose", "up", "--exit-code-from", "mdi_mechanic", "--abort-on-container-exit"],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                cwd=docker_path )
    up_tup = up_proc.communicate()
    up_out = format_return(up_tup[0])
    up_err = format_return(up_tup[1])
    assert up_proc.returncode == 0

    # Run "docker-compose down"
    down_proc = subprocess.Popen( ["docker-compose", "down"],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                cwd=docker_path )
    down_tup = down_proc.communicate()
    down_out = format_return(down_tup[0])
    down_err = format_return(down_tup[1])
    assert down_proc.returncode == 0

def test_unsupported():
    # Get the base directory
    file_path = os.path.dirname(os.path.realpath(__file__))
    base_path = os.path.dirname( os.path.dirname( os.path.dirname( file_path ) ) )
    docker_path = os.path.join( base_path, "MDI_Mechanic", "docker" )

    docker_file = str(base_path) + '/MDI_Mechanic/.temp/docker_mdi_mechanic.sh'
    docker_lines = [ "#!/bin/bash\n",
                     "\n",
                     "# Exit if any command fails\n",
                     "\n",
                     "cd MDI_Mechanic/scripts/drivers\n",
                     "python min_driver.py -command \'UNSUPPORTED\' -nreceive \'MDI_NAME_LENGTH\' -rtype \'MDI_CHAR\' -mdi \'-role DRIVER -name driver -method TCP -port 8021\'\n"]
    os.makedirs(os.path.dirname(docker_file), exist_ok=True)
    with open(docker_file, 'w') as file:
        file.writelines( docker_lines )

    working_dir = str(base_path) + "/user/mdi_tests/test1"
    os.system("rm -rf " + str(base_path) + "/user/mdi_tests/.work")
    os.system("cp -r " + str(working_dir) + " " + str(base_path) + "/user/mdi_tests/.work")

    # Run "docker-compose up"
    up_proc = subprocess.Popen( ["docker-compose", "up", "--exit-code-from", "mdi_mechanic", "--abort-on-container-exit"],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                cwd=docker_path )
    up_tup = up_proc.communicate()
    up_out = format_return(up_tup[0])
    up_err = format_return(up_tup[1])
    assert up_proc.returncode != 0

    # Run "docker-compose down"
    down_proc = subprocess.Popen( ["docker-compose", "down"],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                cwd=docker_path )
    down_tup = down_proc.communicate()
    down_out = format_return(down_tup[0])
    down_err = format_return(down_tup[1])
    assert down_proc.returncode == 0
