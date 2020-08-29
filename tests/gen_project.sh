#! /bin/sh
# Installs cookiecutter in a virtualenv and generates a project with default 
# settings


# Stop execution if a command has a non-zero exit code
set -e

# Create virtualenv if it doesn't exist
if [ ! -d "venv" ]; then
  python3 -m venv venv
fi

source venv/bin/activate

# Install cookiecutter if we don't have it in this virtualenv yet
if ! [ -x "$(command -v cookiecutter)" ]; then
  pip install cookiecutter
fi

# Remove build dir if exist
if [ -d "build" ]; then
  rm -rf build/
fi

# Generate project
cookiecutter -o build/ --no-input .

exit 0
