# -*- coding:utf-8 -*-
# Author:toby
# Date : 2022/2/15 10:43
import flask
from flask import jsonify

app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return jsonify({"code": "1", "msg": "hello toby"})


if __name__ == '__main__':
    app.run(debug=True)