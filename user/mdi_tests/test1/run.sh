#location of required codes
LAMMPS_LOC="${USER_PATH}/lammps/src/lmp_mdi"

#launch LAMMPS
/repo/user/build/lammps/src/lmp_mdi -mdi "${MDI_OPTIONS}" -in lammps.in > lammps.out
