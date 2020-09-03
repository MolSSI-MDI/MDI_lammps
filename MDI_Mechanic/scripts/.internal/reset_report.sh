#!/bin/bash

# Exit if any command fails
set -e

# Obtain the currect working directory
BASE_PATH=$(pwd)

# Create the necessary directories
if [ -d ${BASE_PATH}/report ]; then rm -Rf ${BASE_PATH}/report; fi
cp -r ${BASE_PATH}/MDI_Mechanic/base_report ${BASE_PATH}/report

# Reset the README.md file
cp ${BASE_PATH}/MDI_Mechanic/README.base ${BASE_PATH}/README.md
