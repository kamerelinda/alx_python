from flask import Flask

# creates a flask web application
app = Flask(__name__)


# define the route for the root url with strict slashes false
@app.route('/', strict_slashes=False)
def greetings():
    return "Hello HBNB!"


if __name__ == '__main__':
    # run flask app on 0.0.0.0 and port 5000
    app.run(debug=True, host='0.0.0.0', port=5000)
