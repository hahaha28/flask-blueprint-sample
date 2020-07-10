
from flask import Blueprint

test1 = Blueprint('test1', __name__)


@test1.before_request
def before_request():
    print('test1.before_request')


@test1.route('/view1-test1')
def view1_test1():
    return "view1_test1"