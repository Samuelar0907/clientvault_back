#!/bin/sh

set -e

# Cargar variables de entorno desde el archivo .env
if [ -f .env ]; then
  export $(cat .env | grep -v '^#' | xargs)
fi

echo "Starting server"
pipenv run start
