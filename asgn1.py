from flask import Flask, request, Response

import json
app = Flask(__name__)

@app.route('/distributed', methods=['GET', 'POST'])
def respond_dist():
    if request.method == 'POST':
        return Response('This method is unsupported.', status=405)
    if request.method == 'GET':
        message = '{"Type":"GET","message":"Hello Distributed Systems"}'
        response = Response(message, status=200, mimetype='application/json')
        return response
    return Response('This method is unsupported.', status=405)

@app.route('/systems', methods=['GET', 'POST'])
def respond_syst():
    if request.method == 'POST':
        status = 405
        message = 'This method is unsupported.' 
        if request.args.get('msg'):
            msg = request.args.get('msg')
            message = f'{{"Type":"POST","message":"{msg}"}}'
            status = 200
        response = Response(message, status, mimetype='application/json')
        return response
    if request.method == 'GET':
        message = '{"Type":"GET","message":"Get Message Received"}'
        response = Response(message, status=200, mimetype='application/json')
        return response
    return Response('This method is unsupported.', status=405)
if __name__ == "__main__": 
    app.run(host ='0.0.0.0', port = 8085, debug = True)  