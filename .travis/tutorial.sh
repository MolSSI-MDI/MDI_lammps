#!/bin/sh

# Exit if any command fails
set -e

tutorial_error() {
    # Attempt to push to the remote
    git commit -m "Travis CI commit [ci skip]"
    if git push -v > /dev/null 2>&1 ; then
        echo "Exiting due to error, but was able to push to the remote"
    fi

    exit 1
}

reset_tutorial() {
    cp ./.travis/badges/-failing-red.svg ./.travis/dynamic_badges/step_config.svg
    cp ./.travis/badges/-failing-red.svg ./.travis/dynamic_badges/step_engine_build.svg
    cp ./.travis/badges/-failing-red.svg ./.travis/dynamic_badges/step_mdi_commands.svg
    cp ./.travis/badges/-failing-red.svg ./.travis/dynamic_badges/step_mdi_link.svg
    cp ./.travis/badges/-failing-red.svg ./.travis/dynamic_badges/step_mdi_nodes.svg
    cp ./.travis/badges/-failing-red.svg ./.travis/dynamic_badges/step_min_engine.svg

    git add -u
}

step_config() {
    git remote -v
    if git push -v > /dev/null 2>&1 ; then
        echo "Success: Able to push to remote."
        cp ./.travis/badges/-working-success.svg ./.travis/dynamic_badges/step_config.svg
	git add ./.travis/dynamic_badges/step_config.svg
    else
        echo "Error: Unable to push to remote.  The repo has not been configured correctly."
	tutorial_error
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
git remote -v
git remote set-url origin git@github.com:MolSSI-MDI/MDI_lammps2.git
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

# Attempt to build the engine, using the user-provided script
if ./user/build_engine.sh ; then
    echo "Success: Able to run engine build script."
else
    echo "Error: Unable to build engine"
    tutorial_error
fi

# Verify that the engine has been built / installed correctly
if ./user/validate_build.sh ; then
    echo "Success: Able to verify that engine was built."
    cp ./.travis/badges/-working-success.svg ./.travis/dynamic_badges/step_engine_build.svg
    git add ./.travis/dynamic_badges/step_engine_build.svg
else
    echo "Error: Unable to verify that engine was built."
    tutorial_error
fi

# Commit and push any changes
git commit -m "Travis CI commit [ci skip]"
git push -v > /dev/null 2>&1
