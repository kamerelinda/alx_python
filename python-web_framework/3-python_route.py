""" This module creates a web application with a routing to hbnb """
from flask import Flask


app = Flask(__name__)
""" creates a flask web application """


@app.route('/', strict_slashes=False)
def greetings():
    """ define the route for the root url with strict slashes false """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ define the route for the hbnb url with strict slashes false """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def disp_text(text):
    """ display “C ” followed by the value of the text variable
     and replaces _ with space """
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def disp_py_text(text):
    """ display “python ” followed by is cool
     and replaces _ with space """
    text = text.replace('_', ' ')
    return f"Python {text}"


if __name__ == '__main__':
    # run flask app on 0.0.0.0 and port 5000
    app.run(debug=True, host='0.0.0.0', port=5000)
