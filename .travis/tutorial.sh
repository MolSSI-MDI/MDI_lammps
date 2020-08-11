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
    # Reset the README.md file
    cp ./.travis/README.base ../README.md

    # Reset the badges marking working / failing steps
    cp ./.travis/badges/-failing-red.svg ./.travis/dynamic_badges/step_config.svg
    cp ./.travis/badges/-failing-red.svg ./.travis/dynamic_badges/step_engine_build.svg
    cp ./.travis/badges/-failing-red.svg ./.travis/dynamic_badges/step_engine_test.svg
    cp ./.travis/badges/-failing-red.svg ./.travis/dynamic_badges/step_mdi_commands.svg
    cp ./.travis/badges/-failing-red.svg ./.travis/dynamic_badges/step_mdi_link.svg
    cp ./.travis/badges/-failing-red.svg ./.travis/dynamic_badges/step_mdi_nodes.svg
    cp ./.travis/badges/-failing-red.svg ./.travis/dynamic_badges/step_min_engine.svg
    cp ./.travis/badges/-failing-red.svg ./.travis/dynamic_badges/step_unsupported.svg

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
    bash -e run.sh
}

step_mdi_link() {
    # NOTE: This is temporary, and should be removed later
    ENGINE_EXECUTABLE=${BASE_PATH}/user/lammps/src/lmp_mdi

    # Check if the library is linked dynamically
    #if ldd ${ENGINE_EXECUTABLE} | grep "libmdi." ; then
    if docker run --rm travis/mdi_test ldd /docker_image/lammps/src/lmp_mdi | grep "libmdi." ; then
	echo "The engine is using MDI as a dynamic library"
	return 0
    fi

    # Check if the library is linked statically
    #if nm ${ENGINE_EXECUTABLE} | grep "MDI_Init" ; then
    if docker run --rm travis/mdi_test nm /docker_image/lammps/src/lmp_mdi | grep "MDI_Init" ; then
	echo "The engine is using MDI as a static library"
	return 0
    fi
    return 1
}

step_min_engine() {
    cd ${BASE_PATH}/.travis/codes
    python min_test.py
}

step_unsupported() {
    cd ${BASE_PATH}/.travis/codes
    if python unsupported_test.py ; then
	echo "Error: Script unsupported_test.py ran to completion"
	return 1
    fi
    echo "Success: Script unsupported_test.py threw an error"
    return 0
}

step_mdi_commands() {
    cd ${BASE_PATH}/.travis/codes
    if python check_mdi_commands.py ; then
        echo "Success: Able to determine which MDI commands are supported by this engine"

	# Copy the new README.md file into position
	cp README.temp ${BASE_PATH}/README.md
	git add ${BASE_PATH}/README.md
    else
	echo "Error: Unable to determine which MDI commands are supported by this engine"
	return 1
    fi
}

step_mdi_nodes() {
    cd ${BASE_PATH}/.travis/codes

    if python check_mdi_nodes.py ; then
        echo "Success: Able to determine which MDI nodes are supported by this engine"

	# Copy the new README.md file into position
	cp README.temp ${BASE_PATH}/README.md
	git add ${BASE_PATH}/README.md
        git add ${BASE_PATH}/.travis/graphs/node-report.gv.svg
    else
	echo "Error: Unable to determine which MDI nodes are supported by this engine"
	return 1
    fi
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
#cd user
#if bash -e build_engine.sh ; then
#    echo "Success: Able to run engine build script."
#    cd ${BASE_PATH}
#else
#    echo "Error: Unable to build engine"
#    cd ${BASE_PATH}
#    tutorial_error
#fi

# Verify that the engine has been built / installed correctly
cd user
if bash -e validate_build.sh ; then
    echo "Success: Able to verify that the engine was built."
    cd ${BASE_PATH}
    cp ./.travis/badges/-working-success.svg ./.travis/dynamic_badges/step_engine_build.svg
    git add ./.travis/dynamic_badges/step_engine_build.svg
else
    echo "Error: Unable to verify that the engine was built."
    cd ${BASE_PATH}
    tutorial_error
fi

# Verify that the engine test calculation can be run
if step_engine_test ; then
    echo "Success: Engine test(s) succeeded."
    cd ${BASE_PATH}
    cp ./.travis/badges/-working-success.svg ./.travis/dynamic_badges/step_engine_test.svg
    git add ./.travis/dynamic_badges/step_engine_test.svg
else
    echo "Error: Engine test(s) failed."
    cd ${BASE_PATH}
    tutorial_error
fi

# Check if the engine is linked to the MDI Library
if step_mdi_link ; then
    echo "Success: Engine is linked to the MDI Library."
    cd ${BASE_PATH}
    cp ./.travis/badges/-working-success.svg ./.travis/dynamic_badges/step_mdi_link.svg
    git add ./.travis/dynamic_badges/step_mdi_link.svg
else
    echo "Error: Engine is not linked to the MDI Library."
    cd ${BASE_PATH}
    tutorial_error
fi

# Check if the engine has minimalistic MDI functionality
if step_min_engine ; then
    echo "Success: Engine passed minimal MDI functionality test."
    cd ${BASE_PATH}
    cp ./.travis/badges/-working-success.svg ./.travis/dynamic_badges/step_min_engine.svg
    git add ./.travis/dynamic_badges/step_min_engine.svg
else
    echo "Error: Engine failed minimal MDI functionality test."
    cd ${BASE_PATH}
    tutorial_error
fi

# Check if the engine correctly errors upon receiving an unsupported command
if step_unsupported ; then
    echo "Success: Engine errors out upon receiving an unsupported command."
    cd ${BASE_PATH}
    cp ./.travis/badges/-working-success.svg ./.travis/dynamic_badges/step_unsupported.svg
    git add ./.travis/dynamic_badges/step_unsupported.svg
else
    echo "Error: Engine does not error out upon receiving an unsupported command."
    cd ${BASE_PATH}
    tutorial_error
fi

# Write out the commands that are supported by this engine
if step_mdi_commands ; then
    echo "Success: Detected MDI commands."
    cd ${BASE_PATH}
    cp ./.travis/badges/-working-success.svg ./.travis/dynamic_badges/step_mdi_commands.svg
    git add ./.travis/dynamic_badges/step_mdi_commands.svg
else
    echo "Error: Unable to detect MDI commands."
    cd ${BASE_PATH}
    tutorial_error
fi

# Perform the node analysis
if step_mdi_nodes ; then
    echo "Success: Detected MDI nodes."
    cd ${BASE_PATH}
    cp ./.travis/badges/-working-success.svg ./.travis/dynamic_badges/step_mdi_nodes.svg
    git add ./.travis/dynamic_badges/step_mdi_nodes.svg
else
    echo "Error: Unable to detect MDI nodes."
    cd ${BASE_PATH}
    tutorial_error
fi

# Commit and push any changes
echo "Attempting to commit any changes"
if git commit -m "Travis CI commit [ci skip]" ; then
    echo "Success: Committed final changes to repo"
    git push -v > /dev/null 2>&1
fi
