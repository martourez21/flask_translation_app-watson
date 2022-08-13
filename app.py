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
from machinetranslation.textToSpeech import text_to_voice_out
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
    phrase = [line.replace('\n','') for line in phrase]
    phrase = ''.join(str(line) for line in phrase)
    #text_to_voice_out(phrase)
    try:
        text = english_to_french(model_id, phrase)
        return render_template('index.html', text=text)
    except:

        return render_template('404-page.html');


if __name__ == "__main__":
    app.run(debug=True)
