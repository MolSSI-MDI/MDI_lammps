#!/bin/bash

# Exit if any command fails
set -e

docker build -t travis/mdi_test user
python MDI_Mechanic/scripts/install_engine.py
