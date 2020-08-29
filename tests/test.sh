#! /bin/sh
# This script will generate a project based on this
# cookiecutter and runs its tests

# Stop execution if a command has a non-zero exit code
set -e

# Step 1: generate project
./tests/gen_project.sh

# Step 2: test project
./tests/test_project.sh
