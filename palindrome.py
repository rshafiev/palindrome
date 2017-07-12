#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# coding: utf8

from flask import Flask, request
import json
import re

app = Flask(__name__)

@app.route('/', methods = ['POST'])

def is_palindrome():
    """test API for checking if the word is palindrome.
       get string_id value from JSON request for checking
       Example for curl client:
       $ curl -XPOST -d '{"string_id": "test"}'   -H "Content-Type:application/json"   http://127.0.0.1:8888
       few parameters like:
       $ curl -XPOST -d '{"string_id": "ooppoo", "string2_id": "test"}'   -H "Content-Type:application/json"   http://127.0.0.1:8888
    """
    if "string_id" in request.json:
        string = request.json["string_id"]
    else:
        string = None
    if request.method == 'POST' and string is not None:
        # delete all non-word character, digits, underscores
        string = re.sub(r'[\W\d_]','',string)
        # check if string is equal to reverse string itself
        if string == string[::-1]:
            return string + " is palindrome\n"
        else:
            return string + " is NOT palindrome\n"
    else:
        return "Please provide string_id in JSON\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=False, threaded=True)

