# Obtain dependencies
#sudo apt-get install gfortran
#sudo apt-get install mpich libmpich-dev
#apt-get update && apt-get install -y \
#    gfortran \
#    mpich \
#    libmpich-dev
apt-get update && apt-get install -y \
    gfortran \
    git \
    make

pip install mpi4py
pip install numpy
pip install cmake

export FC=gfortran
pip install -U pytest pytest-cov
