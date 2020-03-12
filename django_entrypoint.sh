#!/usr/bin/env bash

# Migrations
echo "Migrations applying..."
python manage.py migrate

exec "$@"
