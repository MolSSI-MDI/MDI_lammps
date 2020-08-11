#ENGINE_EXECUTABLE=./lammps/src/lmp_mdi
ENGINE_EXECUTABLE=/docker_image/lammps/src/lmp_mdi_
if docker run --rm travis/mdi_test test -f "$ENGINE_EXECUTABLE"; then
    echo "$ENGINE_EXECUTABLE exists"
else
    echo "Could not find engine executable: $ENGINE_EXECUTABLE"
    exit 1
fi
