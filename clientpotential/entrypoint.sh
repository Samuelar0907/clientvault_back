#!/bin/sh

set -e

# Cargar variables de entorno desde el archivo .env
if [ -f .env ]; then
  export $(cat .env | grep -v '^#' | xargs)
fi

DB_HOST2=${POSTGRES_HOST2}
DB_PORT=${POSTGRES_PORT}

/usr/local/bin/wait-for-it.sh "$DB_HOST2:$DB_PORT" --timeout=60 --strict -- echo "PostgreSQL está listo"


echo "Running migrations.."
pipenv run make-migrations

echo "applying migrations "
pipenv run migrate

echo "Starting server"
pipenv run start
