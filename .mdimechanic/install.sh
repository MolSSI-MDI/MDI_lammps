#!/bin/bash

# Exit if any command fails
set -e

install_engine() {
    mdimechanic build
}

if ! install_engine ; then
    export MDI_REPORT_STATUS=1
    cat ./.mdimechanic/ci_badge.md ./README.md > temp && mv temp README.md
    ./.mdimechanic/push_changes.sh
    exit 1
fi
