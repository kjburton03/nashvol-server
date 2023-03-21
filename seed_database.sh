rm db.sqlite3
rm -rf ./nashvolapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations nashvolapi
python3 manage.py migrate nashvolapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata volunteers
python3 manage.py loaddata event_types
python3 manage.py loaddata events
python3 manage.py loaddata event_volunteers
# python3 manage.py loaddata attendees
# Run this command to seed database:    chmod u+x ./seed_database.sh