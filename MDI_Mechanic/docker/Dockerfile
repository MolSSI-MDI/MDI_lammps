# Base docker file for the MDI project
#

FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
        openssh-server \
        python3-dev \
        python3-pip \
        libopenmpi-dev \
    && apt-get clean && apt-get purge && rm -rf /tmp/* /var/tmp/* \
    #
    # Ensure that Python 3 is used by default
    #
    && cd /usr/local/bin \
    && ln -s /usr/bin/python3 python \
    && pip3 install --upgrade pip \
    && rm pip && ln -s /usr/bin/pip3 pip

# ------------------------------------------------------------
# Add an 'mpiexec' user
# ------------------------------------------------------------

ARG MPI_USER=mpiuser
ARG HOME_DIR=/home/${MPI_USER}
ARG SSH_DIR=${HOME_DIR}/.ssh

RUN adduser --disabled-password --gecos "" ${MPI_USER} && \
    echo "${MPI_USER} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# ------------------------------------------------------------
# Set-Up SSH with our Github deploy key
# ------------------------------------------------------------

#RUN mkdir /var/run/sshd \
#    && rm -rf ${SSH_DIR}

RUN mkdir /var/run/sshd \
    && mkdir -p ${SSH_DIR}

COPY ssh/config ${SSH_DIR}/config
COPY ssh/id_rsa.mpi ${SSH_DIR}/id_rsa
COPY ssh/id_rsa.mpi.pub ${SSH_DIR}/id_rsa.pub
COPY ssh/id_rsa.mpi.pub ${SSH_DIR}/authorized_keys

RUN chmod -R 600 ${SSH_DIR}/* && \
    chown -R ${MPI_USER}:${MPI_USER} ${SSH_DIR}

# ------------------------------------------------------------
# Copy MPI4PY example scripts
# ------------------------------------------------------------

CMD ["/usr/sbin/sshd", "-D"]

# ------------------------------------------------------------
# Install MDI_Mechanic-specific dependencies
# ------------------------------------------------------------

RUN apt-get install -y \
        make \
        git \
        cmake \
        graphviz \
    && pip install mpi4py \
    && pip install pandas \
    && pip install PyYAML \
    && pip install graphviz \
    && git clone https://github.com/MolSSI-MDI/MDI_Library.git \
    && mkdir MDI_Library/build \
    && cd MDI_Library/build \
    && cmake -Dlanguage=Python -Dpython_package=ON .. \
    && make && make install \
    && apt-get clean && apt-get purge && rm -rf /tmp/* /var/tmp/*
