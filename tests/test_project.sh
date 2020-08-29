#! /bin/sh

cd build/my_project

# Setup dependencies
./script/bootstrap

# Lint codebase
./script/lint
