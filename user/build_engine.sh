# Obtain dependencies
if [ "$TRAVIS_OS_NAME" == "linux" ]; then
    sudo apt-get install gfortran
    sudo apt-get install mpich libmpich-dev
    sudo pip install mpi4py
    sudo pip install numpy
elif [ "$TRAVIS_OS_NAME" == "osx" ]; then
    brew update > /dev/null
    if [ "$MPI" != "" ]; then
        brew install $MPI
    fi
fi
export FC=gfortran
sudo pip install -U pytest pytest-cov

# Obtain a clone of LAMMPS
git clone https://github.com/MolSSI-MDI/lammps.git
export LAMMPS_INSTALL='serial'
#export LAMMPS_INSTALL='mpi'

# Configure LAMMPS
cd lammps
git checkout mdi
cd src
make yes-standard
make no-gpu
make no-kim
make no-kokkos
make no-kspace
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
python Install.py -m gcc
cd ../../src
  
# Build LAMMPS
if test "${LAMMPS_INSTALL}" = 'serial'; then make mpi-stubs; fi
make -j 4 "${LAMMPS_INSTALL}"
