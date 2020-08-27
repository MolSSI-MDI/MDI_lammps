#!/bin/bash

# Exit if any command fails
set -e

cd MDI_Mechanic/scripts/drivers
python min_driver.py -command \<NAME -nreceive MDI_NAME_LENGTH -rtype MDI_CHAR -mdi '-role DRIVER -name driver -method TCP -port 8021'
