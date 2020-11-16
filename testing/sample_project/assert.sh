#!/bin/bash -e

# cp Pipfile.template Pipfile
# echo "${PYTHON_VERSION:?}" >> Pipfile

# pipenv uninstall tupper

# set +e
# pipenv run python -m tupper
# returned=$?
# set -e

# if [[ "${returned}" != "1" ]]; then
#   echo "Expected tupper execution to fail gracefully: ${returned}"
#   exit 1
# fi

# cauth pipenv install
# pipenv run python -m tupper
