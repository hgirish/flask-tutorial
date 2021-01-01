"""Flask configuration."""

from os import environ, path


basedir = path.abspath(path.dirname(__file__))
"""Set Flask config variables."""
SECRET_KEY = environ.get('SECRET_KEY')
DATABASE = '/home/site/db/flakergo.sqlite'
STATIC_FOLDER = 'static'
TEMPLATES_FOLDER = 'templates'

