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
driver_proc = subprocess.Popen([sys.executable, "unsupported_driver.py", "-mdi", "-role DRIVER -name driver -method TCP -port 8021"],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd="./drivers")

# Run LAMMPS as an engine
os.system("cp -r " + str(working_dir) + " _work")
os.chdir("./_work")
os.system("${USER_PATH}/lammps/src/lmp_mdi -mdi \"-role ENGINE -name TESTCODE -method TCP -port 8021 -hostname localhost\" -in lammps.in > lammps.out")

# Convert the driver's output into a string
driver_tup = driver_proc.communicate()
driver_out = format_return(driver_tup[0])
driver_err = format_return(driver_tup[1])

print("Driver output: ")
print(str(driver_out))

print("Driver error message: ")
print(str(driver_err))

assert driver_err == ""
