from flask import Flask, request, jsonify
from metamaska.metamaska import Metamaska
import base64
import pkg_resources

app = Flask(__name__)

@app.route('/classify', methods=['POST'])
def classify():
    data = request.get_json()
    b64req = data['meta']
    meta = base64.b64decode(b64req).decode('utf-8')

    metamaska = Metamaska()
    prediction = metamaska.form(meta, probability=True)

    response = {
        'attack': prediction[0],
        'type': prediction[1]
    }
    return jsonify(response) 

@app.route('/', methods=['GET'])
def home():
    return 'Goodbye'

@app.route('/environment', methods=['GET'])
def environment():
    installed_packages = pkg_resources.working_set
    installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])
    return '<br>\n'.join(installed_packages_list)

if __name__ == "__main__":
    app.run(port=8001, debug=True)
