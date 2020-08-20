import os
import sys

# Path to this file
file_path = os.path.dirname(os.path.realpath(__file__))

# Path to the top-level directory
base_path = file_path + "/../.."



# Generate the report
os.chdir( str(base_path) )
os.system("./MDI_Mechanic/scripts/.internal/tutorial.sh")
