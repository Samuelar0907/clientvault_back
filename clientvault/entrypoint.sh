#!/bin/sh

set -e

# Cargar variables de entorno desde el archivo .env
if [ -f .env ]; then
  export $(cat .env | grep -v '^#' | xargs)
fi

DB_HOST=${POSTGRES_HOST}
DB_PORT=${POSTGRES_PORT}

TABLE_COMUNA=${TABLE_COMUNA}
TABLE_DIRECCION=${TABLE_DIRECCION}
TABLE_IDENTIFICACION=${TABLE_IDENTIFICACION}
TABLE_OCUPACION=${TABLE_OCUPACION}
TABLE_PACIENTE=${TABLE_PACIENTE}
TABLE_PAIS=${TABLE_PAIS}

TABLE_PREVISION=${TABLE_PREVISION}
TABLE_REGION=${TABLE_REGION}
TABLE_SECTOR=${TABLE_SECTOR}
TABLE_SUCURSAL=${TABLE_SUCURSAL}
TABLE_TELEFONOS=${TABLE_TELEFONOS}
TABLE_NVACADEMICO=${TABLE_NVACADEMICO}

/usr/local/bin/wait-for-it.sh "$DB_HOST:$DB_PORT" --timeout=60 --strict -- echo "PostgreSQL está listo"


# echo "Running migrations.."
# pipenv run make-migrations

echo "applying migrations "
pipenv run migrate



echo "Starting server"
pipenv run start
