[![Build Status](https://github.com/MolSSI-MDI/MDI_lammps2/workflows/CI/badge.svg)](https://github.com/MolSSI-MDI/MDI_lammps2/actions/runs/383529532)
# MDI Mechanic LAMMPS report

This repo presents test results for the MDI interface implementation in the LAMMPS code.

To view the README.md offline, it is suggested that you use grip (i.e., pip install grip).

## Overview of steps

The following lists the basic steps required to run a MDI calculation.
MDI Mechanic will automatically test each of these steps and indicate whether each one is currently working or not.

[comment]: <> (Badges are downloaded from shields.io, i.e.:)
[comment]: <> (curl https://img.shields.io/badge/-working-success --output report/badges/-working-success.svg)

1. ![step2](report/dynamic_badges/step_engine_build.svg) Validate engine build
2. ![step5](report/dynamic_badges/step_min_engine.svg) Implement minimalistic MDI functionality
3. ![step6](report/dynamic_badges/step_unsupported.svg) Correctly respond to unsupported commands
4. ![step8](report/dynamic_badges/step_mdi_nodes.svg) Continue to add support for more MDI commands

## Nodes

The graph indicates which nodes have been implemented in this engine and the connections between them.

![command](report/graphs/node-report.gv.svg)

## Commands

The following table indicates which MDI Standard commands are supported by this engine at each node.
Supported commands are indicated in green, while unsupported commands are indicated in gray.

[travis]: <> ( supported_commands )
## Supported Commands

| | @COORDS | @DEFAULT | @FORCES | @INIT_MD | @INIT_OPTG | @PRE-FORCES |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| &lt;@ | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) |
| &lt;CELL | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) |
| &lt;CELL_DISPL | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) |
| &lt;CHARGES | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) |
| &lt;COORDS | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) |
| &lt;DIMENSIONS | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) |
| &lt;ELEC_MULT | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) |
| &lt;ELEMENTS | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) |
| &lt;ENERGY | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) |
| &lt;FORCES | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) |
| &lt;KE | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) |
| &lt;KE_ELEC | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) |
| &lt;KE_NUC | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) |
| &lt;MASSES | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) |
| &lt;NAME | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) |
| &lt;NATOMS | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) |
| &lt;PE | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) |
| &lt;PE_ELEC | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) |
| &lt;PE_NUC | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) |
| &lt;STRESS | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) |
| &lt;TOTCHARGE | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) |
| &lt;VELOCITIES | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) |
| &gt;+FORCES | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) |
| &gt;CELL | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) |
| &gt;CELL_DISPL | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) |
| &gt;CHARGES | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) |
| &gt;COORDS | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) |
| &gt;ELEC_MULT | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) |
| &gt;FORCES | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) |
| &gt;MASSES | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) |
| &gt;STRESS | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) |
| &gt;TOTCHARGE | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) |
| &gt;VELOCITIES | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) |
| @ | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-brightgreen.svg) |
| @INIT_MD | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) |
| @INIT_OPTG | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-brightgreen.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) |
| EXIT | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) | ![command](report/badges/box-lightgray.svg) |

## Acknowledgements

Badges are obtained from the ![shields.io](https://shields.io/) project.
