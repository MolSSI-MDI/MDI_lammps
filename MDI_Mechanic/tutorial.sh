#!/bin/sh

# Exit if any command fails
set -e

tutorial_error() {
    # Git add all files associated with the documentation
    #git add ${BASE_PATH}/README.md
    #git add ${BASE_PATH}/report

    # Attempt to push to the remote
    #git commit -m "Travis CI commit [ci skip]"
    #if git push -v > /dev/null 2>&1 ; then
    #    echo "Exiting due to error, but was able to push to the remote"
    #fi

    exit 1
}

reset_tutorial() {
    # Create the necessary directories
    if [ -d ${BASE_PATH}/report ]; then rm -Rf ${BASE_PATH}/report; fi
    mkdir -p ${BASE_PATH}/report
    mkdir -p ${BASE_PATH}/report/badges
    mkdir -p ${BASE_PATH}/report/dynamic_badges
    mkdir -p ${BASE_PATH}/report/graphs

    # Reset the README.md file
    cp ${BASE_PATH}/MDI_Mechanic/README.base ${BASE_PATH}/README.md

    # Reset the badges marking working / failing steps
    cp ${BASE_PATH}/MDI_Mechanic/badges/-failing-red.svg ${BASE_PATH}/report/dynamic_badges/step_config.svg
    cp ${BASE_PATH}/MDI_Mechanic/badges/-failing-red.svg ${BASE_PATH}/report/dynamic_badges/step_engine_build.svg
    cp ${BASE_PATH}/MDI_Mechanic/badges/-failing-red.svg ${BASE_PATH}/report/dynamic_badges/step_engine_test.svg
    cp ${BASE_PATH}/MDI_Mechanic/badges/-failing-red.svg ${BASE_PATH}/report/dynamic_badges/step_mdi_commands.svg
    cp ${BASE_PATH}/MDI_Mechanic/badges/-failing-red.svg ${BASE_PATH}/report/dynamic_badges/step_mdi_nodes.svg
    cp ${BASE_PATH}/MDI_Mechanic/badges/-failing-red.svg ${BASE_PATH}/report/dynamic_badges/step_min_engine.svg
    cp ${BASE_PATH}/MDI_Mechanic/badges/-failing-red.svg ${BASE_PATH}/report/dynamic_badges/step_unsupported.svg
}

step_config() {
    git remote -v
    if git push -v > /dev/null 2>&1 ; then
        echo "Success: Able to push to remote."
        cp ${BASE_PATH}/MDI_Mechanic/badges/-working-success.svg ${BASE_PATH}/report/dynamic_badges/step_config.svg
    else
        echo "Error: Unable to push to remote.  The repo has not been configured correctly."
	tutorial_error
    fi
    echo "================================================================="
    git status
    echo "================================================================="
}

step_engine_test() {
    python MDI_Mechanic/scripts/engine_tests.py
}

step_min_engine() {
    cd ${BASE_PATH}/MDI_Mechanic/scripts
    python min_test.py
}

step_unsupported() {
    tutorial_error
    cd ${BASE_PATH}/MDI_Mechanic/scripts
    if python unsupported_test.py ; then
	echo "Error: Script unsupported_test.py ran to completion"
	tutorial_error
    fi
    echo "Success: Script unsupported_test.py threw an error"
    return 0
}

step_mdi_commands() {
    cd ${BASE_PATH}/MDI_Mechanic/scripts
    if python check_mdi_commands.py ; then
        echo "Success: Able to determine which MDI commands are supported by this engine"

	# Copy the new README.md file into position
	cp ${BASE_PATH}/MDI_Mechanic/README.temp ${BASE_PATH}/README.md
    else
	echo "Error: Unable to determine which MDI commands are supported by this engine"
	return 1
    fi
}

step_mdi_nodes() {
    cd ${BASE_PATH}/MDI_Mechanic/scripts

    if python check_mdi_nodes.py ; then
        echo "Success: Able to determine which MDI nodes are supported by this engine"

	# Copy the new README.md file into position
	cp ${BASE_PATH}/MDI_Mechanic/README.temp ${BASE_PATH}/README.md
    else
	echo "Error: Unable to determine which MDI nodes are supported by this engine"
	return 1
    fi
}

# Obtain the currect working directory
BASE_PATH=$(pwd)
export USER_PATH=$(pwd)/user

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
#cd user
#if bash -e validate_build.sh ; then
if python MDI_Mechanic/scripts/validate_build.py ; then
    echo "Success: Able to verify that the engine was built."
    #cd ${BASE_PATH}
    cp ${BASE_PATH}/MDI_Mechanic/badges/-working-success.svg ${BASE_PATH}/report/dynamic_badges/step_engine_build.svg
else
    echo "Error: Unable to verify that the engine was built."
    #cd ${BASE_PATH}
    tutorial_error
fi

# Verify that the engine test calculation can be run
if step_engine_test ; then
    echo "Success: Engine test(s) succeeded."
    cd ${BASE_PATH}
    cp ${BASE_PATH}/MDI_Mechanic/badges/-working-success.svg ${BASE_PATH}/report/dynamic_badges/step_engine_test.svg
else
    echo "Error: Engine test(s) failed."
    cd ${BASE_PATH}
    tutorial_error
fi

# Check if the engine has minimalistic MDI functionality
if step_min_engine ; then
    echo "Success: Engine passed minimal MDI functionality test."
    cd ${BASE_PATH}
    cp ${BASE_PATH}/MDI_Mechanic/badges/-working-success.svg ${BASE_PATH}/report/dynamic_badges/step_min_engine.svg
else
    echo "Error: Engine failed minimal MDI functionality test."
    cd ${BASE_PATH}
    tutorial_error
fi

# Check if the engine correctly errors upon receiving an unsupported command
if step_unsupported ; then
    echo "Success: Engine errors out upon receiving an unsupported command."
    cd ${BASE_PATH}
    cp ${BASE_PATH}/MDI_Mechanic/badges/-working-success.svg ${BASE_PATH}/report/dynamic_badges/step_unsupported.svg
else
    echo "Error: Engine does not error out upon receiving an unsupported command."
    cd ${BASE_PATH}
    tutorial_error
fi

# Write out the commands that are supported by this engine
if step_mdi_commands ; then
    echo "Success: Detected MDI commands."
    cd ${BASE_PATH}
    cp ${BASE_PATH}/MDI_Mechanic/badges/-working-success.svg ${BASE_PATH}/report/dynamic_badges/step_mdi_commands.svg
else
    echo "Error: Unable to detect MDI commands."
    cd ${BASE_PATH}
    tutorial_error
fi

# Perform the node analysis
if step_mdi_nodes ; then
    echo "Success: Detected MDI nodes."
    cd ${BASE_PATH}
    cp ${BASE_PATH}/MDI_Mechanic/badges/-working-success.svg ${BASE_PATH}/report/dynamic_badges/step_mdi_nodes.svg
else
    echo "Error: Unable to detect MDI nodes."
    cd ${BASE_PATH}
    tutorial_error
fi

# Commit and push any changes
#git add ${BASE_PATH}/README.md
#git add ${BASE_PATH}/report
#echo "Attempting to commit any changes"
#if git commit -m "Travis CI commit [ci skip]" ; then
#    echo "Success: Committed final changes to repo"
#    git push -v > /dev/null 2>&1
#fi
