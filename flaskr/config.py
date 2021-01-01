"""Flask configuration."""

from os import environ, path


basedir = path.abspath(path.dirname(__file__))



class Config:
    """Set Flask config variables."""


    SECRET_KEY = environ.get('SECRET_KEY')
    DATABASE = environ.get("DATABASE")
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

