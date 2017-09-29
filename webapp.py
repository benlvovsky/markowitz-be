import markowitz as mark
from flask import Flask
from flask import request
import json
import settings as st
import os

app = Flask(__name__)

@app.route('/health')
def hello_world():
    return '''
    {
    result: OK
    }'''

@app.route('/ef')
def efficientFrontier():
    print ('request source={}'.format(request.args.get('source')))
    print ('request symbols={}'.format(request.args.get('symbols')))
    source = request.args.get('source')
    symbols=request.args.get('symbols')
    if request.args.get('source') is None:
        source = 'google'
    if request.args.get('symbols') is None:
        symbols = ['AAPL', 'GOOG', 'MSFT', 'FB']
    else:
        symbols = request.args.get('symbols').split(",")

    return prettyJson(mark.sharpeAndCml(source = source, symbols = symbols))

@app.route('/upload', methods=['POST'])
def uploadcsv():
    f = request.files['the_file']
    uploadDir = st.config["common"]["upload_directory"]
    
    if not os.path.exists(uploadDir):
        os.makedirs(uploadDir)
    f.save('{}/{}'.format(uploadDir, st.config["common"]["upload_file_name"]))
    return prettyJson(mark.sharpeAndCml('upload', []))

def prettyJson(notPretty):
    parsed = json.loads(notPretty)
    return json.dumps(parsed, indent=4, sort_keys=True)
