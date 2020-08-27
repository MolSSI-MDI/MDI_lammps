import os
import subprocess
import sys

# Path to this file
file_path = os.path.dirname(os.path.realpath(__file__))

# Path to the top-level directory
base_path = file_path + "/.."



# Build the docker image
os.chdir(base_path)
os.system("docker build -t mdi_mechanic/mdi_mechanic docker")
