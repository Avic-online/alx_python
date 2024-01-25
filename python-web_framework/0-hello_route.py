#! /usr/bin/python3
"""
    basic flask web server on avic's
    virtual environment
"""

from flask import Flask 

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def home():
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(debug=True)