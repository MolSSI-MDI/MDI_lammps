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

