# -*- coding: utf-8 -*-
import requests
from flask import Flask, request
app = Flask(__name__)

FLAG = "noxCTF{1_4m_7h3_c4p741n_n0w}\n"
POD_IP = "127.0.0.1"

@app.route('/')
@app.route('/flag') # append something for addess to send the flag to
def PSRF(flag=None, url=None):
	data = ""

	if request.remote_addr == POD_IP:
		if flag:
			try:
				url = request.args.get('url', default = 1, type = str)
				if url == "flag":
						r = requests.post(url, data="{flag}"
						.format(flag=FLAG))
				else:
					data = "¯\_(ツ)_/¯ 'What do you want?'\n"
			except Exception as x:
				return ""

		else:
			data = "( ͡° ͜ʖ ͡°)\n"
	else:
		data = "ಠ_ಠ\n"

	return str(data)

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0', port=1337)