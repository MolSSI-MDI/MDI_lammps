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
| @ | unsupported  |
| &lt;@ | ![command](.travis/badges/box-brightgreen.svg)  |
| &lt;CELL | ![command](.travis/badges/box-brightgreen.svg)  |
| &gt;CELL | unsupported  |
| &lt;CELL_DISPL | unsupported  |
| &gt;CELL_DISPL | unsupported  |
| &lt;CHARGES | ![command](.travis/badges/box-brightgreen.svg)  |
| &gt;CHARGES | unsupported  |
| &lt;COORDS | ![command](.travis/badges/box-brightgreen.svg)  |
| &gt;COORDS | ![command](.travis/badges/box-brightgreen.svg)  |
| &lt;DIMENSIONS | unsupported  |
| &lt;ELEC_MULT | unsupported  |
| &gt;ELEC_MULT | unsupported  |
| &lt;ELEMENTS | unsupported  |
| &lt;ENERGY | ![command](.travis/badges/box-brightgreen.svg)  |
| EXIT | unsupported  |
| &gt;FORCES | ![command](.travis/badges/box-brightgreen.svg)  |
| &gt;+FORCES | unsupported  |
| &lt;FORCES | ![command](.travis/badges/box-brightgreen.svg)  |
| @INIT_MD | ![command](.travis/badges/box-brightgreen.svg)  |
| @INIT_OPTG | unsupported  |
| &lt;KE | unsupported  |
| &lt;KE_ELEC | unsupported  |
| &lt;KE_NUC | unsupported  |
| &lt;MASSES | ![command](.travis/badges/box-brightgreen.svg)  |
| &gt;MASSES | unsupported  |
| &lt;NAME | ![command](.travis/badges/box-brightgreen.svg)  |
| &lt;NATOMS | ![command](.travis/badges/box-brightgreen.svg)  |
| &lt;PE | unsupported  |
| &lt;PE_ELEC | unsupported  |
| &lt;PE_NUC | unsupported  |
| &lt;STRESS | unsupported  |
| &gt;STRESS | unsupported  |
| &lt;TOTCHARGE | unsupported  |
| &gt;TOTCHARGE | unsupported  |
| &lt;VELOCITIES | unsupported  |
| &gt;VELOCITIES | unsupported  |

## Current Step

## Acknowledgements

Badges are obtained from the ![shields.io](https://shields.io/) project.
