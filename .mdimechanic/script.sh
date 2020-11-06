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
    cat ./.travis/travis_badge.md ./README.md > temp && mv temp README.md
    ./.travis/push_changes.sh
    exit 1
fi

# Push any changes to the report
export MDI_REPORT_STATUS=0
./.travis/push_changes.sh
