import mdi
from mdi import MDI_NAME_LENGTH, MDI_COMMAND_LENGTH
import sys

iarg = 1
while iarg < len(sys.argv):
    arg = sys.argv[iarg]

    if arg == "-mdi":
        # Initialize MDI
        if len(sys.argv) <= iarg+1:
            raise Exception("Argument to -mdi option not found")
        mdi.MDI_Init(sys.argv[iarg+1], None)
        iarg += 1
    else:
        raise Exception("Unrecognized argument")

    iarg += 1

# Connect to the engine
comm = mdi.MDI_Accept_Communicator()

# Get the name of the engine, which will be checked and verified at the end
mdi.MDI_Send_Command("<NAME", comm)
initial_name = mdi.MDI_Recv(mdi.MDI_NAME_LENGTH, mdi.MDI_CHAR, comm)

##############
print("AAA")
#mdi.MDI_Send_Command("@INIT_OPTG", comm)
print("BBB")


# Verify that the engine is still responsive
mdi.MDI_Send_Command("<NAME", comm)
final_name = mdi.MDI_Recv(mdi.MDI_NAME_LENGTH, mdi.MDI_CHAR, comm)
assert initial_name == final_name

mdi.MDI_Send_Command("@INIT_MD", comm)
for i in range(100):
    mdi.MDI_Send_Command("@", comm)

mdi.MDI_Send_Command("<ENERGY", comm)
energy = mdi.MDI_Recv(1, mdi.MDI_DOUBLE, comm)
print("Energy: " + str(energy))

mdi.MDI_Send_Command("<PE", comm)
pe = mdi.MDI_Recv(1, mdi.MDI_DOUBLE, comm)
print("PE: " + str(pe))

mdi.MDI_Send_Command("<KE", comm)
ke = mdi.MDI_Recv(1, mdi.MDI_DOUBLE, comm)
print("KE: " + str(ke))

print("CCC")

mdi.MDI_Send_Command("EXIT", comm)
