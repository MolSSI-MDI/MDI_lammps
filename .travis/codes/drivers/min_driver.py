import mdi
import sys

command = None
nreceive = 0
nsend = 0

iarg = 1
while iarg < len(sys.argv):
    arg = sys.argv[iarg]

    if arg == "-mdi":
        # Initialize MDI
        if len(sys.argv) <= iarg+1:
            raise Exception("Argument to -mdi option not found")
        mdi.MDI_Init(sys.argv[iarg+1], None)
        iarg += 1
    elif arg == "-command"
        # Set the command
        if len(sys.argv) <= iarg+1:
            raise Exception("Argument to -command option not found")
        command = sys.argv[iarg+1]
        iarg += 1
    elif arg == "-nreceive":
        # Set the number of elements to receive
        if len(sys.argv) <= iarg+1:
            raise Exception("Argument to -nreceive option not found")
        nreceive = int( sys.argv[iarg+1] )
        iarg += 1
    elif arg == "-nsend":
        # Set the number of elements to send
        if len(sys.argv) <= iarg+1:
            raise Exception("Argument to -nsend option not found")
        nsend = int( sys.argv[iarg+1] )
        iarg += 1
    else:
        raise Exception("Unrecognized argument")

# Connect to the engine
comm = mdi.MDI_Accept_Communicator()

mdi.MDI_Send_Command("<NAME", comm)
name = mdi.MDI_Recv(mdi.MDI_NAME_LENGTH, mdi.MDI_CHAR, comm)

print(" Engine name: " + str(name))

mdi.MDI_Send_Command("EXIT", comm)
