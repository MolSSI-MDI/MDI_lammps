#!/bin/sh

echo "Tutorial"

config_travis() {
  git config --global user.email "travis@travis-ci.com"
  git config --global user.name "Travis CI"
  git checkout ${TRAVIS_BRANCH}

  # Write out the MDI key
  echo "-----BEGIN OPENSSH PRIVATE KEY-----" > travis_key
  echo ${mdi_key} >> travis_key
  echo "-----END OPENSSH PRIVATE KEY-----" >> travis_key
  echo "Host github.com" > ~/.ssh/config
  echo "  IdentityFile  $(pwd)/travis_key" >> ~/.ssh/config
  chmod 400 travis_key

  # Switch the remote to ush ssh
  git remote -v
  git remote set-url origin git@github.com:MolSSI-MDI/MDI_lammps2.git

  echo "After change remote: "
  git remote -v
  echo "================================================================="
  git status
  echo "================================================================="
  git pull
  git push -v
  #git remote add origin-pages https://${mdi_key}@github.com/MolSSI-MDI/MDI_lammps2.git > /dev/null 2>&1
  #git push --quiet --set-upstream origin-pages travis > /dev/null 2>&1
  #git push origin travis
  echo "Making a PR"
}

#git submodule update --remote

if config_travis ; then
    echo "Travis configuration was successful"
else
    echo "Travis configuration was NOT successful"
fi
