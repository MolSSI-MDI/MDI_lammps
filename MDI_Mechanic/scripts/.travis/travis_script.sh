#!/bin/bash

# Exit if any command fails
set -e

source "$HOME/miniconda/etc/profile.d/conda.sh"
conda activate base
./MDI_Mechanic/scripts/.internal/tutorial.sh
