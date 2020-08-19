#!/bin/sh

# Exit if any command fails
set -e

git add ./README.md
git add ./report
git commit -m "Travis CI commit [ci skip]"
git push -v > /dev/null 2>&1

if [ $MDI_REPORT_STATUS==0 ] ; then
    exit 0
else
    exit 1
fi
