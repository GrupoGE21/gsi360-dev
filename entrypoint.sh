#!/bin/sh

echo "Aguardando o PostgreSQL subir..."
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 1
done

echo "PostgreSQL está pronto. Aplicando migrações..."
python manage.py migrate_schemas --shared

echo "Iniciando o servidor..."
python manage.py runserver 0.0.0.0:8000
