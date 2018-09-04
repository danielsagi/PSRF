import requests
import random
import string
from flask import Flask, request, send_file
app = Flask(__name__, static_url_path='')

random_str = lambda: ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(20))

@app.route('/api/v1/upload', methods=["GET"],)
def upload_image():
    method = request.args.get('method', '')
    url = request.args.get('url', '')
    if url and method:
        try:
            if method == "get":
                r = requests.get(url, verify=False)
            elif method == "post":
                r = requests.post(url, verify=False)
            else:
                return "no method specified", 400
            filename = "{}.jpg".format(random_str())
            with open("images/{filename}".format(filename=filename), 'wb') as f:
                f.write(r.content)
            return str(filename), 200
        except Exception as x:
            print x.message
            return "wtf???", 500
    return "wtf", 400

@app.route('/images/<filename>')
def get_image(filename=None):
    if filename:
        return send_file('images/{}'.format(filename), mimetype='image/jpg')
    return "No such file", 404

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=80)
