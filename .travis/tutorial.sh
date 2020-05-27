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
    cp ./.travis/badges/-failing-red.svg ./.travis/dynamic_badges/step_engine_test.svg
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

step_engine_test() {
    cd user/engine_tests/test1
    #./user/engine_tests/test1/run.sh
    ./run.sh
}

# Obtain the currect working directory
BASE_PATH=$(pwd)
export USER_PATH=$(pwd)/user

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
cd user
if ./build_engine.sh ; then
    echo "Success: Able to run engine build script."
else
    echo "Error: Unable to build engine"
    tutorial_error
fi
cd ${BASE_PATH}

# Verify that the engine has been built / installed correctly
cd user
if ./validate_build.sh ; then
    echo "Success: Able to verify that the engine was built."
    cp ./.travis/badges/-working-success.svg ./.travis/dynamic_badges/step_engine_build.svg
    git add ./.travis/dynamic_badges/step_engine_build.svg
else
    echo "Error: Unable to verify that the engine was built."
    tutorial_error
fi
cd ${BASE_PATH}

# Verify that the engine test calculation can be run
cd user
if step_engine_test ; then
    echo "Success: Engine test(s) succeeded."
    cp ./.travis/badges/-working-success.svg ./.travis/dynamic_badges/step_engine_test.svg
    git add ./.travis/dynamic_badges/step_engine_test.svg
else
    echo "Error: Engine test(s) failed."
    tutorial_error
fi
cd ${BASE_PATH}


# Commit and push any changes
if git commit -m "Travis CI commit [ci skip]" ; then
    echo "Success: Committed final changes to repo"
fi
git push -v > /dev/null 2>&1

