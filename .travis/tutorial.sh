#!/bin/sh

echo "Tutorial"

make_pr() {
  git config --global user.email "travis@travis-ci.com"
  git config --global user.name "Travis CI"
  echo "${TRAVIS_BRANCH}"
  echo "=================================================================1"
  git status
  echo "================================================================="
  git checkout ${TRAVIS_BRANCH}
  #git checkout -b travis
  #git submodule update --remote
  #git add -u
  #git commit -m "Submodule update from Travis build $TRAVIS_BUILD_NUMBER"
  echo ${mdi_key} > travis_key
  #ssh-add travis_key
  echo "================================================================="
  git status
  echo "================================================================="
  echo "Host github.com" > ~/.ssh/config
  echo "  IdentityFile  $(pwd)/travis_key" >> ~/.ssh/config
  chmod 400 travis_key
  git remote -v
  git remote set-url origin git@github.com:MolSSI-MDI/MDI_lammps2.git
  echo "After change remote: "
  git remote -v
  #echo "github.com ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCjnaR4zUYVM7Zj3TTc8yzMG6qGzqxO3t70C6Hy/cyt/7QKwCcvwdcs28zcJ1TsSKnoh4w0RQ9xP35WoBrRNQ3JQ3uWC7Yuwaq4KM2f+hdRrF5hhDcYCegPWFbh2sStrMzEi+a+Pyq9ttYE+A0anA1KbMnIyvNyw4wh2EMwLVNE4xxoE/FYQbYK8wLXmvLO3TZdD8EshPiZW6FF/5vT+wRFVdtLJFqjQUJlkH7iqL+rOp05w8bbAeL0ogQIi1ukLCD0us+hWZF+mrvMtCC7eO0zrFoweXwkm2tarMt5KenkIIt8GOyAPvVtROaSIbBFdeYxm4OHP5RmdzdJ5WByC2BP42D30fPFlknqQuwKXSPJ4qxkmCmSxgqMleBcm26Hh6zKIUDnS5hDwQrvxUVGMcy8b7KfKn2iWQnWXZ/r5PJjftSObj1EP8DfIc/ftARdPAORgaHt9wgR4taLLFseJS4J90VzOC4gQj2/b6CRfOdytZY6OYz0P8etYbi8BwEm4fkjDCGYCwn3wXBNRI+7GCgEH4PPCF18sGb70Roh4K68O79p9uF1A3W2jzypXUYlyupVozR8IKrSJnwQuBmi2ySL3luErMag5Fcx+wa93X937XqNqeRmPoGt61rMlBRct0NDO7/RmExnrbFToyHlb61UwhHf7aD5+f2S5xovVhqZYw==" > ~/.ssh/known_hosts
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

make_pr
