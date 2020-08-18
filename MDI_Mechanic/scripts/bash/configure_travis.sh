#!/bin/sh

# Exit if any command fails
set -e

# Write out the MDI key
echo "-----BEGIN OPENSSH PRIVATE KEY-----" > travis_key
echo ${mdi_key} >> travis_key
echo "-----END OPENSSH PRIVATE KEY-----" >> travis_key
echo "Host github.com" > ~/.ssh/config
echo "  IdentityFile  $(pwd)/travis_key" >> ~/.ssh/config
chmod 400 travis_key

# Configure Travis to use Git
git config --global user.email "travis@travis-ci.com"
git config --global user.name "Travis CI"

# Switch the remote to use ssh
git remote -v
git remote set-url origin git@github.com:MolSSI-MDI/MDI_lammps2.git
git checkout ${TRAVIS_BRANCH}
