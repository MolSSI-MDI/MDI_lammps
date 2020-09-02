#!/bin/bash

# Exit if any command fails
set -e

install_engine() {
   docker build -t travis/mdi_test user
   python MDI_Mechanic/scripts/install_engine.py
}

if ! install_engine ; then
    export MDI_REPORT_STATUS=1
    ./MDI_Mechanic/scripts/.internal/push_changes.sh
    exit 1
fi
