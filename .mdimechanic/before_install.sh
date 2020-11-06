#!/bin/bash

# Exit if any command fails
set -e

configure_git() {
    # Write out the MDI key
    #echo "-----BEGIN OPENSSH PRIVATE KEY-----" > travis_key
    #echo ${mdi_key} >> travis_key
    #echo "-----END OPENSSH PRIVATE KEY-----" >> travis_key
    #echo "Host github.com" > ~/.ssh/config
    #echo "  IdentityFile  $(pwd)/travis_key" >> ~/.ssh/config
    #chmod 400 travis_key

    # Configure Travis to use Git
    git config --global user.email "action@github.com"
    git config --global user.name "GitHub Action"

    # Switch the remote to use ssh
    #git remote -v
    #git remote set-url origin git@github.com:MolSSI-MDI/MDI_lammps2.git
    #git checkout ${TRAVIS_BRANCH}

    # Confirm that Travis can push
    git remote -v
    git push -v > /dev/null 2>&1

    # Set the Travis CI badge
    mkdir -p .travis
    echo "![Build Status Actions](https://github.com/MolSSI-MDI/MDI_lammps2/workflows/CI/badge.svg)" > ./.travis/travis_badge.md
}

install_dependencies() {
    # Update apt-get
    sudo apt-get update

    # Install pyyaml
    pip install pyyaml

    # Install MDI Mechanic
    mkdir mechbuild
    cd mechbuild
    git clone https://github.com/MolSSI-MDI/MDI_Mechanic.git
    cd MDI_Mechanic
    pip install .
    cd ../..
}

if ! configure_git ; then
    exit 1
fi

#if ! install_dependencies ; then
if install_dependencies ; then
    export MDI_REPORT_STATUS=1
    cat ./.travis/travis_badge.md ./README.md > temp && mv temp README.md
    ./.travis/push_changes.sh
    exit 1
fi
