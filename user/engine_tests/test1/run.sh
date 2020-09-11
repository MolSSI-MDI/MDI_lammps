#location of required codes
#LAMMPS_LOC="${USER_PATH}/lammps/src/lmp_mdi"
#LAMMPS_LOC="/docker_image/lammps/src/lmp_mdi"
LAMMPS_LOC="/repo/user/build/lammps/src/lmp_mdi"
echo "IN run.sh:"
echo "USER PATH: "
echo ${USER_PATH}
#echo "LAMMPS_LOC: "
#echo ${LAMMPS_LOC}
#echo "Checking for file: "
#ls ${LAMMPS_LOC}
echo "Working directory: "
pwd
ls


#set the number of threads
#export OMP_NUM_THREADS=1

#launch LAMMPS
${LAMMPS_LOC} -in lammps.in > lammps.out

echo "Test output: "
cat lammps.out
