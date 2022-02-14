# @Time : 2022/1/18 21:56 
# @Author :jiale
# @File : web_server_flask.py 
# @Software: PyCharm
import flask
from flask import jsonify

app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return jsonify({"code": "1", "msg": "hello toby"})


if __name__ == '__main__':
    app.run(debug=True)
