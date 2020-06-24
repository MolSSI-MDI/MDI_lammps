import os
import sys
import subprocess
from graphviz import Digraph

def format_return(input_string):
    my_string = input_string.decode('utf-8')

    # remove any \r special characters, which sometimes are added on Windows
    my_string = my_string.replace('\r','')

    return my_string

def test_nodes():
    port_num = 9001
    mdi_driver_options = "-role DRIVER -name driver -method TCP -port " + str(port_num)

    # Get the number of nodes
    driver_proc = subprocess.Popen([sys.executable, "min_driver.py", "-command", "<NNODES", 
                                    "-nreceive", "1", "-rtype", "MDI_INT", 
                                    "-mdi", mdi_driver_options],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd="./drivers")

    # Run LAMMPS as an engine
    mdi_engine_options = "-role ENGINE -name TESTCODE -method TCP -hostname localhost -port " + str(port_num)
    working_dir = "../../user/mdi_tests/test1"
    os.system("rm -rf ./_work")
    os.system("cp -r " + str(working_dir) + " _work")
    os.chdir("./_work")
    os.system("${USER_PATH}/lammps/src/lmp_mdi -mdi \"" + str(mdi_engine_options) + "\" -in lammps.in > lammps.out")
    os.chdir("../")

    #user_path = os.system("echo ${USER_PATH}")
    #engine_path = str(user_path) + "/lammps/src/lmp_mdi"
    #print( "Environment: " + str(os.environ) )
    #engine_proc = subprocess.Popen(["${USER_PATH}/lammps/src/lmp_mdi", 
    #                                "-mdi", mdi_driver_options, 
    #                                "-in", "lammps.in"], 
    #                                shell=True, 
    #                                env=dict(os.environ), 
    #                                stdout=subprocess.PIPE, 
    #                                stderr=subprocess.PIPE, 
    #                                cwd="./_work")
    
    user_path = os.system("echo ${USER_PATH}")
    engine_path = str(user_path) + "/lammps/src/lmp_mdi"
    print( "Environment: " + str(os.environ) )
    engine_proc = subprocess.Popen(["echo", "${USER_PATH}/lammps/src/lmp_mdi"], 
                                    shell=True, 
                                    env=dict(os.environ), 
                                    stdout=subprocess.PIPE, 
                                    stderr=subprocess.PIPE, 
                                    cwd="./_work")

    # Convert the driver's output into a string
    driver_tup = driver_proc.communicate()
    driver_out = format_return(driver_tup[0])
    driver_err = format_return(driver_tup[1])

    engine_tup = engine_proc.communicate()
    engine_out = format_return(engine_tup[0])
    engine_err = format_return(engine_tup[1])
    print("   Engine out: " + str(engine_out))
    print("   Engine err: " + str(engine_err))

    print("CHECK_MDI_NODES.PY")
    print("   Driver out: " + str(driver_out))
    print("   Driver err: " + str(driver_err))



test_nodes()

dot = Digraph(comment='Node Report', format='svg')

dot.node('@DEFAULT', '@DEFAULT')
dot.node('@INIT_MD', '@INIT_MD')
dot.node('@INIT_OPTG', '@INIT_OPTG')
dot.node('@INIT_MC', '@INIT_MC')
dot.node('@INIT_MD_', '@PRE-FORCES\n@FORCES\n@COORDS')
dot.node('@INIT_OPTG_', '@PRE-FORCES\n@FORCES\n@COORDS')

dot.edge('@DEFAULT', '@INIT_MD')
dot.edge('@DEFAULT', '@INIT_OPTG')
dot.edge('@DEFAULT', '@INIT_MC')
dot.edge('@INIT_MD', '@INIT_MD_')
dot.edge('@INIT_OPTG', '@INIT_OPTG_')

dot.render('../graphs/node-report.gv')
