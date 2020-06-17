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

@ unsupported  
&lt;@ supported  
&lt;CELL supported  
&gt;CELL unsupported  
&lt;CELL_DISPL unsupported  
&gt;CELL_DISPL unsupported  
&lt;CHARGES supported  
&gt;CHARGES unsupported  
&lt;COORDS supported  
&gt;COORDS supported  
&lt;DIMENSIONS unsupported  
&lt;ELEC_MULT unsupported  
&gt;ELEC_MULT unsupported  
&lt;ELEMENTS unsupported  
&lt;ENERGY supported  
EXIT unsupported  
&gt;FORCES supported  
&gt;+FORCES unsupported  
&lt;FORCES supported  
@INIT_MD supported  
@INIT_OPTG unsupported  
&lt;KE unsupported  
&lt;KE_ELEC unsupported  
&lt;KE_NUC unsupported  
&lt;MASSES supported  
&gt;MASSES unsupported  
&lt;NAME supported  
&lt;NATOMS supported  
&lt;PE unsupported  
&lt;PE_ELEC unsupported  
&lt;PE_NUC unsupported  
&lt;STRESS unsupported  
&gt;STRESS unsupported  
&lt;TOTCHARGE unsupported  
&gt;TOTCHARGE unsupported  
&lt;VELOCITIES unsupported  
&gt;VELOCITIES unsupported  

## Current Step

## Acknowledgements

Badges are obtained from the ![shields.io](https://shields.io/) project.