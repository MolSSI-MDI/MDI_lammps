ENGINE_EXECUTABLE=./lammps/src/lmp_"${LAMMPS_INSTALL}"
if test -f "$ENGINE_EXECUTABLE"; then
    echo "$ENGINE_EXECUTABLE exists"
else
    echo "Could not find engine executable: $ENGINE_EXECUTABLE"
    exit 1
fi
