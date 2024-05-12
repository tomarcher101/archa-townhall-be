# Instructions

1. Install [Python 3.12](https://www.python.org/downloads/).
2. Install [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).
3. Create a virtualenv in this directory `python -m virtualenv venv`.
4. Activate the virtualenv `source venv/bin/activate`.
5. Install the project dependencies `pip install -r requirements.txt`.
6. Run the database migrations `python townhallproject/manage.py migrate`.
7. Run the Django server `python townhallproject/manage.py runserver`.
