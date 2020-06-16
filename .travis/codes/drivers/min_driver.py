import mdi
import sys

command = None
nreceive = None
rtype = None
nsend = None
stype = None

iarg = 1
while iarg < len(sys.argv):
    arg = sys.argv[iarg]

    if arg == "-mdi":
        # Initialize MDI
        if len(sys.argv) <= iarg+1:
            raise Exception("Argument to -mdi option not found")
        mdi.MDI_Init(sys.argv[iarg+1], None)
        iarg += 1
    elif arg == "-command":
        # Set the command
        if len(sys.argv) <= iarg+1:
            raise Exception("Argument to -command option not found")
        command = sys.argv[iarg+1]
        iarg += 1
    elif arg == "-nreceive":
        # Set the number of elements to receive
        if len(sys.argv) <= iarg+1:
            raise Exception("Argument to -nreceive option not found")
        nreceive = sys.argv[iarg+1]
        iarg += 1
    elif arg == "-nsend":
        # Set the number of elements to send
        if len(sys.argv) <= iarg+1:
            raise Exception("Argument to -nsend option not found")
        nsend = sys.argv[iarg+1]
        iarg += 1
    elif arg == "-rtype":
        # Set the type of elements to receive
        if len(sys.argv) <= iarg+1:
            raise Exception("Argument to -rtype option not found")
        rtype = sys.argv[iarg+1]
        iarg += 1
    elif arg == "-stype":
        # Set the type of elements to receive
        if len(sys.argv) <= iarg+1:
            raise Exception("Argument to -stype option not found")
        stype = sys.argv[iarg+1]
        iarg += 1
    else:
        raise Exception("Unrecognized argument")

    iarg += 1

recv_type = None
if nreceive is not None:
    # Confirm that the receive type is valid
    if rtype == "MDI_CHAR":
        recv_type = mdi.MDI_CHAR
    elif rtype == "MDI_INT":
        recv_type = mdi.MDI_INT
    elif rtype == "MDI_DOUBLE":
        recv_type = mdi.MDI_DOUBLE
    elif rtype == "MDI_BYTE":
        recv_type = mdi.MDI_BYTE
    else:
        raise Exception("Invalid receive type")
        
send_type = None
if nsend is not None:
    # Confirm that the receive type is valid
    if stype == "MDI_CHAR":
        send_type = mdi.MDI_CHAR
    elif stype == "MDI_INT":
        send_type = mdi.MDI_INT
    elif stype == "MDI_DOUBLE":
        send_type = mdi.MDI_DOUBLE
    elif stype == "MDI_BYTE":
        send_type = mdi.MDI_BYTE
    else:
        raise Exception("Invalid receive type")

# Connect to the engine
comm = mdi.MDI_Accept_Communicator()

mdi.MDI_Send_Command("<NAME", comm)
name = mdi.MDI_Recv(mdi.MDI_NAME_LENGTH, mdi.MDI_CHAR, comm)

print(" Engine name: " + str(name))

mdi.MDI_Send_Command("EXIT", comm)
