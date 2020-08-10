import mdi
import os
import sys
import subprocess

def format_return(input_string):
    my_string = input_string.decode('utf-8')

    # remove any \r special characters, which sometimes are added on Windows
    my_string = my_string.replace('\r','')

    return my_string

working_dir = "../../user/mdi_tests/test1"

engine_name = "${USER_PATH}/lammps/src/lmp_mdi"

# Launch the driver in the background
driver_proc = subprocess.Popen([sys.executable, "min_driver.py", "-command", "UNSUPPORTED", "-mdi", "-role DRIVER -name driver -method TCP -port 8021"],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd="./drivers")

# Run LAMMPS as an engine
#os.system("cp -r " + str(working_dir) + " _work")
#os.chdir("./_work")
#os.system("${USER_PATH}/lammps/src/lmp_mdi -mdi \"-role ENGINE -name TESTCODE -method TCP -port 8021 -hostname localhost\" -in lammps.in > lammps.out")

# Use Docker to run the engine
os.system("rm -rf ${USER_PATH}/_work")
os.system("cp -r " + str(working_dir) + " ${USER_PATH}/_work")
mdi_engine_options = "-role ENGINE -name TESTCODE -method TCP -hostname localhost -port 8021"
docker_string = "docker run --net=host --rm -v ${USER_PATH}/_work:/data -it travis/mdi_test bash -c \"cd /data && ls && /docker_image/lammps/src/lmp_mdi -mdi \'" + mdi_engine_options + "\' -in lammps.in > lammps.out\""
os.system(docker_string)


# Convert the driver's output into a string
driver_tup = driver_proc.communicate()
driver_out = format_return(driver_tup[0])
driver_err = format_return(driver_tup[1])

print("Driver output: ")
print(str(driver_out))

print("Driver error message: ")
print(str(driver_err))

assert driver_err == ""
