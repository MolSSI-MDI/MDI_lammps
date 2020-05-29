# MDI_lammps2

Test repo for lammps engine.

To clone with submodules:

git clone --recurse-submodules https://github.com/MolSSI-MDI/MDI_lammps2.git

To update submodules:

git submodule update --remote

## Overview of steps

[comment]: <> (Badges are downloaded from shields.io, i.e.:)
[comment]: <> (curl https://img.shields.io/badge/-working-success --output .travis/badges/-working-success.svg)

1. ![step1](.travis/dynamic_badges/step_config.svg) Configure repo
2. ![step2](.travis/dynamic_badges/step_engine_build.svg) Build engine
3. ![step3](.travis/dynamic_badges/step_engine_test.svg) Add engine test(s)
4. ![step4](.travis/dynamic_badges/step_mdi_link.svg) Link to the MDI Library
5. ![step5](.travis/dynamic_badges/step_min_engine.svg) Implement minimalistic engine functionality
6. ![step6](.travis/dynamic_badges/step_unsupported.svg) Error on unsupported commands
7. ![step7](.travis/dynamic_badges/step_mdi_commands.svg) Add support for more MDI commands
8. ![step8](.travis/dynamic_badges/step_mdi_nodes.svg) Add support for the MDI Node System

## Current Step

## Acknowledgements

Badges are obtained from the ![shields.io](https://shields.io/) project.