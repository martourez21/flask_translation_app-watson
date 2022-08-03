"""
This is the start of this application

Returns:
    _type_: _description_
"""
from flask import Flask, render_template
from machinetranslation.translator import english_to_french, french_to_english
import json


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    """Function to load the home page of this application

    Returns:
        _type_: _description_
    """
    text = english_to_french("Apr 13, 2021 · The package python-dotenv installed earlier is used to load them instead of having to pass each variable in the terminal before typing flask run. When you run the application, you should see Home. 2. Configure the application. Install flask-sqlalchemy, flask-migrate. They are needed to run and manage your database.")
    return render_template('index.html', text=text)


if __name__ == "__main__":
    app.run(debug=True)
