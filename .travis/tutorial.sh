#!/bin/sh

echo "Tutorial"

make_pr() {
  git config --global user.email "travis@travis-ci.com"
  git config --global user.name "Travis CI"
  git checkout -b travis
  git submodule update --remote
  git add -u
  git commit -m "Submodule update from Travis build $TRAVIS_BUILD_NUMBER"
  #git push origin travis
  echo "Making a PR"
}

#git submodule update --remote

make_pr
