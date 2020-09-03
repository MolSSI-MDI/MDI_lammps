#!/bin/bash

# Exit if any command fails
set -e

tutorial_error() {
    exit 1
}

step_engine_test() {
    python MDI_Mechanic/scripts/.internal/engine_tests.py
}

step_min_engine() {
    cd ${BASE_PATH}/MDI_Mechanic/scripts/.internal
    python min_test.py
}

step_unsupported() {
    cd ${BASE_PATH}/MDI_Mechanic/scripts/.internal
    if python unsupported_test.py ; then
	echo "Error: Script unsupported_test.py ran to completion"
	tutorial_error
    fi
    echo "Success: Script unsupported_test.py threw an error"
    return 0
}

step_mdi_nodes() {
    cd ${BASE_PATH}/MDI_Mechanic/scripts/.internal

    if python check_mdi_nodes.py ; then
        echo "Success: Able to determine which MDI nodes are supported by this engine"

	# Copy the new README.md file into position
	cp ${BASE_PATH}/MDI_Mechanic/.temp/README.temp ${BASE_PATH}/README.md
    else
	echo "Error: Unable to determine which MDI nodes are supported by this engine"
	return 1
    fi
}

# Obtain the currect working directory
BASE_PATH=$(pwd)
export USER_PATH=$(pwd)/user

#git submodule update --remote

# Verify that the engine has been built / installed correctly
if python MDI_Mechanic/scripts/.internal/validate_build.py ; then
    echo "Success: Able to verify that the engine was built."
    cp ${BASE_PATH}/report/badges/-working-success.svg ${BASE_PATH}/report/dynamic_badges/step_engine_build.svg
else
    echo "Error: Unable to verify that the engine was built."
    tutorial_error
fi

# Verify that the engine test calculation can be run
if step_engine_test ; then
    echo "Success: Engine test(s) succeeded."
    cd ${BASE_PATH}
    cp ${BASE_PATH}/report/badges/-working-success.svg ${BASE_PATH}/report/dynamic_badges/step_engine_test.svg
else
    echo "Error: Engine test(s) failed."
    cd ${BASE_PATH}
    tutorial_error
fi

# Check if the engine has minimalistic MDI functionality
if step_min_engine ; then
    echo "Success: Engine passed minimal MDI functionality test."
    cd ${BASE_PATH}
    cp ${BASE_PATH}/report/badges/-working-success.svg ${BASE_PATH}/report/dynamic_badges/step_min_engine.svg
else
    echo "Error: Engine failed minimal MDI functionality test."
    cd ${BASE_PATH}
    tutorial_error
fi

# Check if the engine correctly errors upon receiving an unsupported command
if step_unsupported ; then
    echo "Success: Engine errors out upon receiving an unsupported command."
    cd ${BASE_PATH}
    cp ${BASE_PATH}/report/badges/-working-success.svg ${BASE_PATH}/report/dynamic_badges/step_unsupported.svg
else
    echo "Error: Engine does not error out upon receiving an unsupported command."
    cd ${BASE_PATH}
    tutorial_error
fi

# Perform the node analysis
if step_mdi_nodes ; then
    echo "Success: Detected MDI nodes."
    cd ${BASE_PATH}
    cp ${BASE_PATH}/report/badges/-working-success.svg ${BASE_PATH}/report/dynamic_badges/step_mdi_nodes.svg
else
    echo "Error: Unable to detect MDI nodes."
    cd ${BASE_PATH}
    tutorial_error
fi
