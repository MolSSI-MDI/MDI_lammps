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

[travis]: <> ( supported_commands )
## Supported Commands

| | @DEFAULT |
| ------------- | ------------- |
| @ | ![command](.travis/badges/box-lightgray.svg)  |
| &lt;@ | ![command](.travis/badges/box-brightgreen.svg)  |
| &lt;CELL | ![command](.travis/badges/box-brightgreen.svg)  |
| &gt;CELL | ![command](.travis/badges/box-lightgray.svg)  |
| &lt;CELL_DISPL | ![command](.travis/badges/box-lightgray.svg)  |
| &gt;CELL_DISPL | ![command](.travis/badges/box-lightgray.svg)  |
| &lt;CHARGES | ![command](.travis/badges/box-brightgreen.svg)  |
| &gt;CHARGES | ![command](.travis/badges/box-lightgray.svg)  |
| &lt;COORDS | ![command](.travis/badges/box-brightgreen.svg)  |
| &gt;COORDS | ![command](.travis/badges/box-brightgreen.svg)  |
| &lt;DIMENSIONS | ![command](.travis/badges/box-lightgray.svg)  |
| &lt;ELEC_MULT | ![command](.travis/badges/box-lightgray.svg)  |
| &gt;ELEC_MULT | ![command](.travis/badges/box-lightgray.svg)  |
| &lt;ELEMENTS | ![command](.travis/badges/box-lightgray.svg)  |
| &lt;ENERGY | ![command](.travis/badges/box-brightgreen.svg)  |
| EXIT | ![command](.travis/badges/box-lightgray.svg)  |
| &gt;FORCES | ![command](.travis/badges/box-brightgreen.svg)  |
| &gt;+FORCES | ![command](.travis/badges/box-lightgray.svg)  |
| &lt;FORCES | ![command](.travis/badges/box-brightgreen.svg)  |
| @INIT_MD | ![command](.travis/badges/box-brightgreen.svg)  |
| @INIT_OPTG | ![command](.travis/badges/box-lightgray.svg)  |
| &lt;KE | ![command](.travis/badges/box-lightgray.svg)  |
| &lt;KE_ELEC | ![command](.travis/badges/box-lightgray.svg)  |
| &lt;KE_NUC | ![command](.travis/badges/box-lightgray.svg)  |
| &lt;MASSES | ![command](.travis/badges/box-brightgreen.svg)  |
| &gt;MASSES | ![command](.travis/badges/box-lightgray.svg)  |
| &lt;NAME | ![command](.travis/badges/box-brightgreen.svg)  |
| &lt;NATOMS | ![command](.travis/badges/box-brightgreen.svg)  |
| &lt;PE | ![command](.travis/badges/box-lightgray.svg)  |
| &lt;PE_ELEC | ![command](.travis/badges/box-lightgray.svg)  |
| &lt;PE_NUC | ![command](.travis/badges/box-lightgray.svg)  |
| &lt;STRESS | ![command](.travis/badges/box-lightgray.svg)  |
| &gt;STRESS | ![command](.travis/badges/box-lightgray.svg)  |
| &lt;TOTCHARGE | ![command](.travis/badges/box-lightgray.svg)  |
| &gt;TOTCHARGE | ![command](.travis/badges/box-lightgray.svg)  |
| &lt;VELOCITIES | ![command](.travis/badges/box-lightgray.svg)  |
| &gt;VELOCITIES | ![command](.travis/badges/box-lightgray.svg)  |

## Current Step

## Acknowledgements

Badges are obtained from the ![shields.io](https://shields.io/) project.
