#!/bin/sh

echo "Tutorial"

make_pr() {
  git config --global user.email "travis@travis-ci.com"
  git config --global user.name "Travis CI"
  echo "Making a PR"
}

git submodule update --remote

make_pr
