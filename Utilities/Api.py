from flask import *
import jsonify, time, os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
  return json.dumps({"cs v1"})

@app.route('/api/v1/send_bytes', methods=['POST'])
def send_bytes():

  print(request)

  return '', 204  
  
app.run(host = "127.0.0.1", port=1337)