import os
import sys

# Path to this file
file_path = os.path.dirname(os.path.realpath(__file__))

# Path to the top-level directory
base_path = file_path + "/../.."



# Generate the report
os.chdir( str(base_path) )
os.system("./MDI_Mechanic/scripts/.internal/reset_report.sh")
os.system("./MDI_Mechanic/scripts/.internal/tutorial.sh")

# Prepend the Travis badge
readme_path = os.path.join(base_path, "README.md")
badge_path = os.path.join(base_path, ".travis", "travis_badge.md")
badge = None
readme = None
with open(badge_path, 'r') as original: badge = original.read()
with open(readme_path, 'r') as original: readme = original.read()
with open(readme_path, 'w') as modified: modified.write(badge + readme)
