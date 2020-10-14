#------------------------------------------------------------#
# Docker file for MDI Mechanic
#------------------------------------------------------------#

FROM mdi/base

RUN apt-get update -y && \
    apt-get install -y \
        git \
        cmake \
        graphviz \
        && \
    apt-get clean && \
    apt-get purge && \
    rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/* && \
    pip install mpi4py && \
    pip install pandas && \
    pip install PyYAML && \
    pip install graphviz && \
    #
    #--------------------------------------------------------#
    # Build the MDI Library
    #--------------------------------------------------------#
    #
    git clone https://github.com/MolSSI-MDI/MDI_Library.git && \
    mkdir MDI_Library/build && \
    cd MDI_Library/build && \
    cmake -Dlanguage=Python -Dpython_package=ON .. && \
    make && \
    make install && \
    cd ../../ && \
    rm -rf MDI_Library
