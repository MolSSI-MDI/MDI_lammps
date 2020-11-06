#!/bin/bash

# Exit if any command fails
set -e

run_tests() {
    # Run the script to generate the MDI report
    if mdimechanic report ; then
        echo "Report script succeeded."
	return 0
    else
        echo "Report script failed."
	return 1
    fi
}

if ! run_tests ; then
    export MDI_REPORT_STATUS=1
    cat ./.mdimechanic/ci_badge.md ./README.md > temp && mv temp README.md
    ./.mdimechanic/push_changes.sh
    exit 1
fi

# Push any changes to the report
echo "Pushing completed report"
export MDI_REPORT_STATUS=0
./.mdimechanic/push_changes.sh
