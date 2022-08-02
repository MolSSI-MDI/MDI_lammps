from mpi4py import MPI
import numpy as np
import mdi

class MDIExecutor:
    def __init__(self,comm=None):
        self.coords=None
        self.atypes=None
        self.box=None
        self.energy=None
        self.forces=None
        if comm is None:
            comm=MPI.COMM_SELF
        self.comm=comm

    def single_point(self,mdiargs,plugin,plugin_args,box,atypes,coords):
        try:
            mdi.MDI_Init(mdiargs)
        except:
            pass
        self.box=box
        self.atypes=atypes
        self.coords=coords
        mdi.MDI_Launch_plugin(plugin,plugin_args,self.comm,self.perform_single_point,None)
        return self.energy,self.forces

    def perform_single_point(self,world,mdicomm,dummy):
        me = world.Get_rank()
        nprocs = world.Get_size()
        print("ME: ",me," OF ",nprocs,type(world),type(mdicomm),flush=True)

        if not self.coords is None and not self.box is None and not self.atypes is None:
            natoms=int(np.array(self.coords).shape[0]/3)
            self.forces=np.zeros(3*natoms,dtype=np.float64)
            print("IN",flush=True)
            mdi.MDI_Send_command(">CELL",mdicomm)
            mdi.MDI_Send(self.box,9,mdi.MDI_DOUBLE,mdicomm)

            mdi.MDI_Send_command(">NATOMS",mdicomm)
            mdi.MDI_Send(natoms,1,mdi.MDI_INT,mdicomm)
            mdi.MDI_Send_command(">TYPES",mdicomm)
            mdi.MDI_Send(self.atypes,natoms,mdi.MDI_INT,mdicomm)
            mdi.MDI_Send_command(">COORDS",mdicomm)
            mdi.MDI_Send(self.coords,3*natoms,mdi.MDI_DOUBLE,mdicomm)

            mdi.MDI_Send_command("<PE",mdicomm)
            self.energy = mdi.MDI_Recv(1,mdi.MDI_DOUBLE,mdicomm)
            self.energy = world.bcast(self.energy,root=0)

            mdi.MDI_Send_command("<FORCES",mdicomm)
            mdi.MDI_Recv(3*natoms,mdi.MDI_DOUBLE,mdicomm,buf=self.forces)
            world.Bcast(self.forces,root=0)

        else:
            print("ERROR!")
            self.energy=None
            self.forces=None
        print("OUT",flush=True)
        mdi.MDI_Send_command("EXIT",mdicomm)
        print("RETURN",flush=True)
        return 0


mdiargs="-role DRIVER -name sequence -method LINK -plugin_path /users/d_perez/chicoma-local/src/lammps/build/install/Lammps-Chicoma_CPU/lib64/"
plugin="lammps"
plugin_args="-log log.sequence -in /users/d_perez/chicoma-local/src/parsplice/sample-input/mdi/modules/in.sequence -mdi \"-role ENGINE -name lammps -method LINK\""



box=[1,0,0]+[0,1,0]+[0,0,1]
atypes=[1]
coords=[1,1,1]


world=MPI.COMM_WORLD
me = world.Get_rank()

comm=world.Split(color=me)


########mdi.MDI_Init(mdiargs)
#if me==0:  <- HANGS in LAMMPS Initialization!
#if True: <- WORKS!
if me==0:
    executor=MDIExecutor(comm=comm)
    executor.single_point(mdiargs,plugin,plugin_args,box,atypes,coords)

