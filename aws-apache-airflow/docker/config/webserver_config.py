# -*- coding: utf-8 -*-

"""Default configuration for the Airflow webserver"""

import os
from airflow import configuration as conf
from flask_appbuilder.security.manager import AUTH_DB

basedir = os.path.abspath(os.path.dirname(__file__))

# The SQLAlchemy connection string.
SQLALCHEMY_DATABASE_URI = conf.get('core', 'SQL_ALCHEMY_CONN')

# Flask-WTF flag for CSRF
CSRF_ENABLED = True

# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = False

# The authentication type
AUTH_TYPE = AUTH_DB