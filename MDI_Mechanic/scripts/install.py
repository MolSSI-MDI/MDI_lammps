import os
import utils.utils as ut

# Path to the user directory
base_path = ut.get_base_path()

# Switch to the base directory
os.chdir(base_path)

# Build the MDI base image
ret = os.system("docker build -t mdi/base MDI_Mechanic/docker/base")
if ret != 0:
    raise Exception("Unable to build the MDI Mechanic image")

# Build the MDI Mechanic image
ret = os.system("docker build -t mdi_mechanic/mdi_mechanic MDI_Mechanic/docker")
if ret != 0:
    raise Exception("Unable to build the MDI Mechanic image")

# Build the engine image
ret = os.system("docker build -t mdi_mechanic/lammps user/docker")
if ret != 0:
    raise Exception("Unable to build the engine image")

# Build the engine, within its Docker image
docker_string = "docker run --rm -v " + str(base_path) + ":/repo -it mdi_mechanic/lammps bash -c \"cd /repo/user/docker && ls && ./docker_install.sh\""
os.system(docker_string)
