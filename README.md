# Instructions

1. Install [Python 3.12](https://www.python.org/downloads/).
2. Install [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).
3. Create a virtualenv in this directory `python -m virtualenv venv`.
4. Activate the virtualenv `source venv/bin/activate`.
5. Install the project dependencies `pip install -r requirements.txt`.
6. Run the database migrations `python townhallproject/manage.py migrate`.
7. Add the address you are running the FE on to `CORS_ORIGIN_WHITELIST` in `settings.py`.
8. Run the Django server `python townhallproject/manage.py runserver`.

# Exposing server

9. Add the address you are running the FE on to `ALLOWED_HOSTS` in `settings.py`.
10. Install [ngrok](https://ngrok.com/).
11. Keep Django running and on a new terminal run `ngrok [port you are exposing Django server on]`.
