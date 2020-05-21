#!/bin/sh

echo "Tutorial"

make_pr() {
  git config --global user.email "travis@travis-ci.com"
  git config --global user.name "Travis CI"
  git checkout -b travis
  git submodule update --remote
  git add -u
  git commit -m "Submodule update from Travis build $TRAVIS_BUILD_NUMBER"
  git remote add origin-pages https://${mdi_key}@github.com/MolSSI-MDI/MDI_lammps2.git > /dev/null 2>&1
  #git push --quiet --set-upstream origin-pages travis > /dev/null 2>&1
  #git push origin travis
  echo "Making a PR"
}

#git submodule update --remote

make_pr
