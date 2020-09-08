import os
import sys
import yaml

# Path to this file
file_path = os.path.dirname(os.path.realpath(__file__))

# Path to the top-level directory
base_path = file_path + "/../.."



# Run the engine, using Docker
docker_string = "docker run --rm -v " + str(base_path) + ":/repo -it travis/mdi_test bash -c \"cd /repo/user && ls && ./docker_install.sh\""
command_string = str(file_path) + "/utils/generate_ssh_keys.sh"
os.system(command_string)
