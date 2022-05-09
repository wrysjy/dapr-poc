import flask
from flask import request
from flask_cors import CORS
import json

app = flask.Flask(__name__)
CORS(app)


# subscribe to the topic
@app.route('/dsstatus', methods=['POST'])
def ds_subscriber():
    # data = request.get_json()
    print("PubSub received a message!", flush=True)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


app.run()
