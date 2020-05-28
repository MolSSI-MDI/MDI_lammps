import sys
import mdi

mdi.MDI_Init(sys.argv[2],mpi_world)

# Connect to the engine
comm = mdi.MDI_Accept_Communicator()

mdi.MDI_Send_Command("<NAME", comm)
name = mdi.MDI_Recv(mdi.MDI_NAME_LENGTH, mdi.MDI_CHAR, comm)

print(" Engine name: " + str(name))

mdi.MDI_Send_Command("EXIT", comm)
