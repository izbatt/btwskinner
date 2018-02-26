from flask import Flask, request, abort, make_response, send_file
import urllib
import json
import os 


app = Flask(__name__)

@app.route("/")
def hello():
    return "running"
    
@app.route('/player/<username>', methods=['GET']) #localhost:8877/player
def getImage(username):
    print(username)
    if os.path.isfile(username):
        return send_file(username, as_attachment=True)
    else:
        print(username+" does not exist on server")




if __name__ == '__main__':
    port = int(os.getenv('PORT', 8877))
    app.run(debug=True, port=port, host='0.0.0.0')