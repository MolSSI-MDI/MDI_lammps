#import mdi

import os
import subprocess

working_dir = "../../user/engine_tests/test1"

os.system("cp -r " + str(working_dir) + " _work")
os.chdir("./_work")

engine_name = "${USER_PATH}/lammps/src/lmp_mdi"

os.system("ls ${USER_PATH}/lammps/src/lmp_mdi")
os.system("echo $USER_PATH")
os.system("echo $BASE_PATH")
os.system("pwd")

# Run LAMMPS by itself
#os.system("${USER_PATH}/lammps/src/lmp_mdi -in lammps.in > lammps.out")

#driver_proc = subprocess.Popen([driver_name, "-mdi", "-role DRIVER -name driver -method TCP -port 8021"],
#                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#engine_proc = subprocess.Popen([engine_name, "-mdi", "-role ENGINE -name MM -method TCP -port 8021 -hostname localhost"])
#engine_proc = subprocess.Popen([engine_name, "-in", "lammps.in",">","lammps.out"])
#engine_proc = subprocess.Popen([engine_name, "-in", "lammps.in"])
#driver_tup = driver_proc.communicate()
#engine_proc.communicate()

# Launch the driver in the background
driver_proc = subprocess.Popen([sys.executable, "./drivers/min_driver.py", "-mdi", "-role DRIVER -name driver -method TCP -port 8021"],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=build_dir)

# Run LAMMPS as an engine
os.system("${USER_PATH}/lammps/src/lmp_mdi -mdi \"-role ENGINE -name TESTCODE -method TCP -port 8021 -hostname localhost\" -in lammps.in > lammps.out")

driver_tup = driver_proc.communicate()

print("Hello World!")
