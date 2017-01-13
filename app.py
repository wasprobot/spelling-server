#!/usr/bin/env python

import urllib
import json
import os
import math

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def processRequest(req):
    result = req.get("result")
    params = result.get("parameters")
    alphabet = params.get("alphabet")
    spelling = ''.join(alphabet)

    next_word = requests.post('http://watchout4snakes.com/wo4snakes/Random/RandomWord').content

    return {
        "speech": next_word,
        "displayText": next_word,
        "data": next_word,
        # "contextOut": [{"name":"spelling-server", "lifespan":2, "parameters":{"current_word": "You said " + spelling}}],
        "source": "spelling-server"
    }

    # return {
    #     "speech": "You said " + spelling,
    #     "displayText": "You said " + spelling,
    #     "data": "You said " + spelling,
    #     # "contextOut": [{"name":"spelling-server", "lifespan":2, "parameters":{"current_word": "You said " + spelling}}],
    #     "source": "spelling-server"
    # }

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=False, port=port, host='0.0.0.0')
