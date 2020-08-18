import os
import subprocess
import sys
import yaml

# Path to this file
file_path = os.path.dirname(os.path.realpath(__file__))

# Path to the top-level directory
base_path = file_path + "/../.."



# Run the engine, using Docker
docker_string = "docker run --rm -v " + str(base_path) + ":/repo -it travis/mdi_test bash -c \"cd /repo/user && ls && ./docker_install.sh\""
os.system(docker_string)
