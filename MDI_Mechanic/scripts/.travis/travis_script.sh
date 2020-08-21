#!/bin/bash

# Exit if any command fails
set -e

source "$HOME/miniconda/etc/profile.d/conda.sh"
conda activate base

# Run the script to generate the MDI report
#./MDI_Mechanic/scripts/.internal/tutorial.sh
if ./MDI_Mechanic/scripts/.internal/tutorial.sh ; then
    echo "Report script succeeded."
    export MDI_REPORT_STATUS=0
else
    echo "Report script failed."
    export MDI_REPORT_STATUS=1
fi

# Push any changes to the report
./MDI_Mechanic/scripts/.internal/push_changes.sh
