#!/bin/bash

# Exit if any command fails
set -e

run_tests() {
    source "$HOME/miniconda/etc/profile.d/conda.sh"
    conda activate base

    # Run the script to generate the MDI report
    if python ./MDI_Mechanic/scripts/report.py ; then
        echo "Report script succeeded."
	return 0
    else
        echo "Report script failed."
	return 1
    fi
}

if ! run_tests ; then
    export MDI_REPORT_STATUS=1
    ./MDI_Mechanic/scripts/.travis/push_changes.sh
    exit 1
fi

# Push any changes to the report
export MDI_REPORT_STATUS=0
./MDI_Mechanic/scripts/.travis/push_changes.sh
