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

@app.route("/number_template/<int:n>", strict_slashes=False)
def template_number(n):
    return render_template("5-number.html", n=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_compare(n):
    # yeild = "even" if n % 2 == 0 else "odd"
    if n % 2 == 0:
        yeild = "even" 
        return render_template("6-number_odd_or_even.html", n=n, yeild=yeild)
    else:
        yeild = "odd"
        return render_template("6-number_odd_or_even.html", n=n, yeild=yeild)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")