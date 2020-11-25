#!/bin/bash

# Exit if any command fails
set -e

configure_git() {
    # Configure Git
    git config --global user.email "action@github.com"
    git config --global user.name "GitHub Action"
    git config pull.ff only

    # Confirm that the build can push
    git remote -v
    git push -v > /dev/null 2>&1

    # Pull, in case this build was restarted
    git pull

    # Set the CI badge
    #echo "[![Build Status](${GITHUB_SERVER_URL}/${GITHUB_REPOSITORY}/workflows/CI/badge.svg)](${GITHUB_SERVER_URL}/${GITHUB_REPOSITORY}/actions/runs/${GITHUB_RUN_ID})" > ./.mdimechanic/ci_badge.md
    echo "[![Build Status](${GITHUB_SERVER_URL}/${GITHUB_REPOSITORY}/workflows/CI/badge.svg)](${GITHUB_SERVER_URL}/${GITHUB_REPOSITORY}/actions/)" > ./.mdimechanic/ci_badge.md
}

install_dependencies() {
    # Update apt-get
    sudo apt-get update

    # Install pyyaml
    pip install wheel
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

if ! install_dependencies ; then
    export MDI_REPORT_STATUS=1
    cat ./.mdimechanic/ci_badge.md ./README.md > temp && mv temp README.md
    ./.mdimechanic/push_changes.sh
    exit 1
fi
