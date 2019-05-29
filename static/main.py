#!/usr/local/bin/python3.6

import flask
from flask import Flask, request

from quaternion import *

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")

HELLO = "Hello, anonymous! Would you like to input your name?"

name_param = None

def hello():
	if request.method == 'GET':
		isget_param="GET!"
		ispost_param=""
		name_param=request.args.get('name')
	elif request.method == 'POST':
		isget_param=""
		ispost_param="POST!"
		name_param=request.form.get('name')
	else:
		name_param=None

	if name_param == None or name_param == "":
		hello_param=HELLO
	else:
		hello_param="Hello," + name_param + "!"

	return name_param, hello_param, isget_param, ispost_param

@app.route('/', methods=['GET', 'POST'])
def root():
	name_param, hello_param, isget_param, ispost_param = hello()
	return flask.render_template(
		'index.html',
		name=name_param,
		hello=hello_param,
		isget=isget_param,
		ispost=ispost_param
	)

@app.route('/name', methods=['GET', 'POST'])
def name():
	name_param, hello_param, isget_param, ispost_param = hello()
	return flask.render_template(
		'name.html',
		name=name_param,
		hello=hello_param,
		isget=isget_param,
		ispost=ispost_param
	)

@app.route('/base', methods=['GET', 'POST'])
def base():
	name_param, hello_param, isget_param, ispost_param = hello()
	return flask.render_template(
		'base.html',
		name=name_param,
		hello=hello_param,
		isget=isget_param,
		ispost=ispost_param
	)

if __name__ == '__main__':
	app.run()
