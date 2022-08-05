"""
This is the start of this application

Returns:
    _type_: _description_
"""
from base64 import encode
from flask import Flask, request, render_template
from urllib.parse import quote

import urllib3
from machinetranslation.translator import english_to_french, french_to_english
import json


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    """Function to load the home page of this application
    Returns:
        _type_: _description_
    """
    return render_template('index.html')

@app.route('/translate')
def translation():
    phrase = request.args.get("textToTranslate")
    _model1 = request.args.get("mode_id1")
    _model2 = request.args.get("mode_id2")
    print("##############################")
    print(phrase)
    model_id = _model1 + '-' +_model2
    print(model_id)

    text = english_to_french(model_id, phrase)
    
    return render_template('index.html', text=text)


if __name__ == "__main__":
    app.run(debug=True)
