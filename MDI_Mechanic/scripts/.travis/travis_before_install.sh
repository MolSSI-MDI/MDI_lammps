#!/bin/bash

# Exit if any command fails
set -e

configure_git() {
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

    # Confirm that Travis can push
    git remote -v
    git push -v > /dev/null 2>&1

    # Set the Travis CI badge
    mkdir -p .travis
    echo "[![Build Status](${TRAVIS_BUILD_WEB_URL%/builds*}.svg?branch=master)](${TRAVIS_BUILD_WEB_URL%/builds*})" > ./.travis/travis_badge.md
    #git add ./.travis/travis_badge.md || true
    #git commit -m "Travis CI commit [ci skip]" || true
    #git push -v > /dev/null 2>&1
}

reset_report() {
    # Run the script to reset the MDI report
    if python3 ./MDI_Mechanic/scripts/utils/reset_report.py ; then
        echo "Report reset succeeded."
	return 0
    else
        echo "Report reset failed."
	return 1
    fi
}

install_dependencies() {
    # Update apt-get
    sudo apt-get update

    # Install conda
    #wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
    #bash miniconda.sh -b -p $HOME/miniconda
    #source "$HOME/miniconda/etc/profile.d/conda.sh"
    #export PATH=$HOME/miniconda/bin:$PATH
    #conda config --set always_yes yes --set changeps1 no
    #conda update -q conda
    #conda info -a

    # Install pymdi
    #conda activate base
    #conda install -c conda-forge pymdi pyyaml pandas python-graphviz
    #conda info -a

    # Create the MDI_Mechanic docker image
    #python MDI_Mechanic/scripts/install_mechanic.py

    # Install MDI Mechanic
    git clone https://github.com/MolSSI-MDI/MDI_Mechanic.git
    cd MDI_Mechanic
    pip install .
}

if ! configure_git ; then
    exit 1
fi

#if ! reset_report ; then
#    exit 1
#fi

if ! install_dependencies ; then
    export MDI_REPORT_STATUS=1
    cat ./.travis/travis_badge.md ./README.md > temp && mv temp README.md
    ./MDI_Mechanic/scripts/.travis/push_changes.sh
    exit 1
fi
