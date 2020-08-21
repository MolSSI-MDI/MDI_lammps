import mdi
import os
import sys
import subprocess

# Path to this file
file_path = os.path.dirname(os.path.realpath(__file__))

# Path to the top-level directory
base_path = file_path + "/../.."

# Platform-specific hostname
if sys.platform == "darwin":
    hostname = "host.docker.internal"
else:
    hostname = "localhost"



def format_return(input_string):
    my_string = input_string.decode('utf-8')

    # remove any \r special characters, which sometimes are added on Windows
    my_string = my_string.replace('\r','')

    return my_string

# Launch the driver in the background
driver_proc = subprocess.Popen([sys.executable, "min_driver.py", "-command", "<NAME", "-nreceive", "MDI_NAME_LENGTH", "-rtype", "MDI_CHAR", "-mdi", "-role DRIVER -name driver -method TCP -port 8021"],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd="./drivers")

# Run the engine, using Docker
mdi_engine_options = "-role ENGINE -name TESTCODE -method TCP -hostname " + str(hostname) +" -port 8021"
working_dir = str(base_path) + "/user/mdi_tests/test1"
os.system("rm -rf " + str(base_path) + "/.work")
os.system("cp -r " + str(working_dir) + " " + str(base_path) + "/.work")
docker_string = "docker run --net=host --rm -v " + str(base_path) + ":/repo -it travis/mdi_test bash -c \"cd /repo/.work && ls && export MDI_OPTIONS=\'" + str(mdi_engine_options) + "\' && ./run.sh\""
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
