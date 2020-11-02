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

if ! install_dependencies ; then
    export MDI_REPORT_STATUS=1
    cat ./.travis/travis_badge.md ./README.md > temp && mv temp README.md
    ./.travis/push_changes.sh
    exit 1
fi
