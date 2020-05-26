#!/bin/sh

# Exit if any command fails
set -e

reset_tutorial() {
    cp ./.travis/badges/-failing-red.svg ./.travis/dynamic_badges/step_config.svg
    cp ./.travis/badges/-failing-red.svg ./.travis/dynamic_badges/step_engine_build.svg
    cp ./.travis/badges/-failing-red.svg ./.travis/dynamic_badges/step_mdi_commands.svg
    cp ./.travis/badges/-failing-red.svg ./.travis/dynamic_badges/step_mdi_link.svg
    cp ./.travis/badges/-failing-red.svg ./.travis/dynamic_badges/step_mdi_nodes.svg
    cp ./.travis/badges/-failing-red.svg ./.travis/dynamic_badges/step_min_engine.svg
}

step_config() {
    git remote -v
    #git pull
    if git push -v ; then
	echo "AAAAA PUSH WORKED"
	cp ./.travis/badges/-working-success.svg ./.travis/dynamic_badges/step_config.svg
    else
	echo "BBBBB PUSH FAILED"
    fi
    echo "================================================================="
    git status
    echo "================================================================="
    #git remote add origin-pages https://${mdi_key}@github.com/MolSSI-MDI/MDI_lammps2.git > /dev/null 2>&1
    #git push --quiet --set-upstream origin-pages travis > /dev/null 2>&1
    #git push origin travis
}

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
#git remote -v
#git remote set-url origin git@github.com:MolSSI-MDI/MDI_lammps2.git
git checkout ${TRAVIS_BRANCH}

# Reset the tutorial
reset_tutorial

# Test whether the repo has been correctly configured
step_config

config_travis() {
  echo "Making a PR"
}

#git submodule update --remote

config_travis
if [ "$?" = "0" ]; then
    echo "Travis configuration was successful"
else
    echo "Travis configuration was NOT successful"
fi
