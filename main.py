from flask import Flask, request, jsonify, render_template, redirect, url_for
import pandas as pd
import numpy as np
from datetime import datetime
import os
from groq import Groq
from fuzzywuzzy import fuzz, process
from question_process import generate_response, ask_groq, clean_response
# Đặt API key của bạn từ GroqCloud ở đây

app = Flask(__name__)

@app.route('/')
def home():
    return 1
@app.route('/ask', methods=['POST'])
def ask():
     if request.method == 'POST':
        data = request.get_json()
        ask_value = data.get('ask', None)
        answer = generate_response(ask_value)
        response = {
            'message': 'JSON received!',
            'data': answer
        }
        return response
    
if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=2999)