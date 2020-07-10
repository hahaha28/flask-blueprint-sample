from flask import Flask
from view1.test1 import test1

app = Flask(__name__)
app.register_blueprint(test1)

@app.before_request
def before_request():
    print("app.before_request")

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
