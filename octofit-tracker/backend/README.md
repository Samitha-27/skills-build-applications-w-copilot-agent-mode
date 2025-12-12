OctoFit Tracker Backend
=======================

Setup
-----

Create a Python virtual environment and install the requirements:

```bash
python3 -m venv octofit-tracker/backend/venv
source octofit-tracker/backend/venv/bin/activate
pip install -r octofit-tracker/backend/requirements.txt
```

Follow the project instructions for additional setup such as MongoDB and Django configuration.
Populate the database using the management command after installing dependencies:

```bash
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata
python manage.py populate_db
```

