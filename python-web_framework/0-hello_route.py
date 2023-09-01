""" This module creates a flask web application """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def greetings():
    """ define the route for the root url with strict slashes false """
    return "Hello HBNB"


if __name__ == '__main__':
    # run flask app on 0.0.0.0 and port 5000
    app.run(debug=True, host='0.0.0.0', port=5000)
