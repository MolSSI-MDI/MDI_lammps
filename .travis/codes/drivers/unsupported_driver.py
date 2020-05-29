import mdi
import sys

mdi.MDI_Init(sys.argv[2], None)

# Connect to the engine
comm = mdi.MDI_Accept_Communicator()

mdi.MDI_Send_Command("UNSUPPORTED", comm)

print(" Engine name: " + str(name))

mdi.MDI_Send_Command("EXIT", comm)
