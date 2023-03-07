rm -rf server/migrations
rm db.sqlite3
python3 manage.py migrate
python3 manage.py makemigrations harmoniousapi
python3 manage.py migrate harmoniousapi
python3 manage.py loaddata users
python3 manage.py loaddata melodyTextures
python3 manage.py loaddata chords
python3 manage.py loaddata chordProgressions
python3 manage.py loaddata soundscapes
python3 manage.py loaddata soundscapeChordProgressions
# chmod +x seed.sh
# ./seed.sh
