from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    return '''<h1>My api</h1>'''

@app.route('/api/', methods=['GET'])
def api():
    return jsonify({'msg': 'hello from flask'})

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)