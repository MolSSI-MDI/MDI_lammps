#!/bin/bash

# Exit if any command fails
set -e

# Set Travis CI badge
echo "[![Build Status](${TRAVIS_BUILD_WEB_URL%/builds*}.svg?branch=master)](${TRAVIS_BUILD_WEB_URL%/builds*})"

# Write out the MDI key
echo "-----BEGIN OPENSSH PRIVATE KEY-----" > travis_key
echo ${mdi_key} >> travis_key
echo "-----END OPENSSH PRIVATE KEY-----" >> travis_key
echo "Host github.com" > ~/.ssh/config
echo "  IdentityFile  $(pwd)/travis_key" >> ~/.ssh/config
chmod 400 travis_key

# Configure Travis to use Git
git config --global user.email "travis@travis-ci.com"
git config --global user.name "Travis CI"

# Switch the remote to use ssh
git remote -v
git remote set-url origin git@github.com:MolSSI-MDI/MDI_lammps2.git
git checkout ${TRAVIS_BRANCH}

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

# Create the MDI_Mechanic docker image
python MDI_Mechanic/scripts/install_mechanic.py
