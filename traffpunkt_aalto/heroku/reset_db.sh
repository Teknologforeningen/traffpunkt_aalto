#!/bin/bash
heroku pg:reset DATABASE

echo "Running syncdb"
heroku run python manage.py syncdb --all

echo "Migrating"
heroku run python manage.py migrate --fake
echo "Done"