#location of required codes
#LAMMPS_LOC=$(cat ../../../locations/LAMMPS)
#LAMMPS_LOC=../../../lammps/src/lmp_mdi
LAMMPS_LOC=${USER_PATH}/lammps/src/lmp_mdi
echo "IN run.sh:"
echo "USER PATH: "
echo ${USER_PATH}
echo "LAMMPS_LOC: "
echo ${LAMMPS_PATH}
pwd
ls


#set the number of threads
#export OMP_NUM_THREADS=1

#launch LAMMPS
#${LAMMPS_LOC} -mdi "-role ENGINE -name MM -method TCP -port 8021 -hostname localhost" -in lammps.in > lammps.out

${LAMMPS_LOC} -in lammps.in > lammps.out
