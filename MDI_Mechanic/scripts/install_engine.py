import os
import sys
import yaml

# Path to this file
file_path = os.path.dirname(os.path.realpath(__file__))
base_path = os.path.dirname( os.path.dirname( file_path ) )

# Build the docker image
#os.system("docker build -t travis/mdi_test user")

# Run the engine, using Docker
docker_string = "docker run --rm -v " + str(base_path) + ":/repo -it travis/mdi_test bash -c \"cd /repo/user && ls && ./docker_install.sh\""
os.system(docker_string)
