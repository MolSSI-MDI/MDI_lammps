#!/bin/sh

# Exit if any command fails
set -e

# Confirm that Travis can push
git remote -v
git push -v > /dev/null 2>&1

# Add the configuration success badge to the report
#cp ./MDI_Mechanic/badges/-working-success.svg ./report/dynamic_badges/step_config.svg
