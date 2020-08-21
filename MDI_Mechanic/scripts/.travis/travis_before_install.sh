#!/bin/bash

# Exit if any command fails
set -e

# Update apt-get
sudo apt-get update

# Install conda
wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
bash miniconda.sh -b -p $HOME/miniconda
source "$HOME/miniconda/etc/profile.d/conda.sh"
export PATH=$HOME/miniconda/bin:$PATH
conda config --set always_yes yes --set changeps1 no
conda update -q conda
conda info -a

# Install pymdi
conda activate base
conda install -c conda-forge pymdi pyyaml pandas python-graphviz
conda info -a
