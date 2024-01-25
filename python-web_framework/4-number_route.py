#! /usr/bin/python3
"""
    basic flask web server on avic's
    virtual environment
"""

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes=False

@app.route("/", strict_slashes=False)
def home():
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    formatted_text = text.replace('_', ' ')
    return f"C {formatted_text}"
    # return render_template("copy_route.html", formatted_text=formatted_text)

@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    formatted_text = text.replace('_', ' ')
    return f"Python {formatted_text}"
    # return render_template("python_route.html", formatted_text=formatted_text)

@app.route("/python", strict_slashes=False)
def python_noslash():
    return "Python is cool"

@app.route("/python/", strict_slashes=False)
def python_slash():
    return "Python is cool"

@app.route("/number/<int:n>", strict_slashes=False)
def python_number(n):
    # formatted_text = text.replace('_', ' ')
    return f"{n} is a number"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")