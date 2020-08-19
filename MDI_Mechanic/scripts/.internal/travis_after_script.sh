#!/bin/sh

# Exit if any command fails
set -e

git add ./README.md || true
git add ./report || true
git commit -m "Travis CI commit [ci skip]" || true
git push -v > /dev/null 2>&1

echo "Finished pushing the updated report."
echo ${MDI_REPORT_STATUS}

if [ ${MDI_REPORT_STATUS}==0 ] ; then
    echo "Success. The report has been pushed."
    exit 0
else
    echo "The report script failed, but the update has been successfully pushed."
    exit 1
fi
