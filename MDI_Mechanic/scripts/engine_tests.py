import os

# Change directory to this file's location
file_path = os.path.dirname(os.path.realpath(__file__))

# Path to the top-level directory
base_path = file_path + "/../.."

# Run the engine test script
working_dir = str(base_path) + "/user/engine_tests/test1"
os.system("rm -rf " + str(base_path) + "/.work")
os.system("cp -r " + str(working_dir) + " " + str(base_path) + "/.work")
bash_command = "docker run --net=host --rm -v " + str(base_path) + ":/repo -it travis/mdi_test bash -c \"cd /repo/.work && ./run.sh\""
ret = os.system(bash_command)
if ret != 0:
    raise Exception("Engine test script returned non-zero value.")
