import os

# Change directory to this file's location
file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(file_path)

# Construct the absolute path to the repo's top-level directory
top_dir = os.getcwd() + "/../../"

# Run the engine test script
bash_command = "docker run --net=host --rm -v " + str(top_dir) + ":/repo -it travis/mdi_test bash -c \"cd /repo/user && ./validate_build.sh\""
return os.system(bash_command)
