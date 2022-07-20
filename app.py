"""
This is the start of this application

Returns:
    _type_: _description_
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """Function to load the home page of this application

    Returns:
        _type_: _description_
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
