import mdi
import os
import sys
import subprocess

# Path to this file
file_path = os.path.dirname(os.path.realpath(__file__))

# Path to the top-level directory
base_path = file_path + "/../.."

working_dir = str(base_path) + "/user/mdi_tests/test1"
os.system("rm -rf " + str(base_path) + "/user/mdi_tests/.work")
os.system("cp -r " + str(working_dir) + " " + str(base_path) + "/user/mdi_tests/.work")
os.chdir(str(base_path) + "/MDI_Mechanic/docker")

ret = os.system("docker-compose up --exit-code-from mdi_mechanic --abort-on-container-exit")
assert ret == 0

ret = os.system("docker-compose down")
assert ret == 0
