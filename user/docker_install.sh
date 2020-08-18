# Obtain a clone of LAMMPS
git clone https://github.com/MolSSI-MDI/lammps.git build/lammps
LAMMPS_INSTALL='serial'
#LAMMPS_INSTALL='mpi'

# Configure LAMMPS
cd build/lammps
git checkout mdi
cd src
make yes-standard
make no-gpu
make no-kim
make no-kokkos
#make no-kspace
make no-latte
make no-meam
make no-mpiio
make no-mscg
make no-poems
make no-python
make no-reax
make no-voronoi
make no-user-qmmm
make yes-user-mdi
cd ../lib/mdi
#python Install.py -m gcc
make -f Makefile.gcc
cd ../../src
  
# Build LAMMPS
if test "${LAMMPS_INSTALL}" = 'serial'; then make mpi-stubs; fi
make -j 4 "${LAMMPS_INSTALL}"
cp lmp_"${LAMMPS_INSTALL}" lmp_mdi
