from os import environ

from flask import (
    Blueprint, current_app
)




bp = Blueprint('test', __name__)

@bp.route("/test")
def test():
  database = environ.get('DATABASE')
  database = current_app.config['DATABASE']
  return "DATABASE is at : %s" % (database, )
