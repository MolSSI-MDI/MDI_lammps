#!/bin/bash

# Exit if any command fails
set -e

install_engine() {
   #docker build -t mdi_mechanic/lammps user
   python3 MDI_Mechanic/scripts/install.py
}

if ! install_engine ; then
    export MDI_REPORT_STATUS=1
    cat ./.travis/travis_badge.md ./README.md > temp && mv temp README.md
    ./MDI_Mechanic/scripts/.travis/push_changes.sh
    exit 1
fi
