# -*- coding: utf-8 -*-
import requests
from flask import Flask, request
app = Flask(__name__)

FLAG = "noxCTF{1_4m_7h3_c4p741n_n0w}\n"
POD_IP = "127.0.0.1"

@app.route('/')
@app.route('/flag') # append something for addess to send the flag to
def PSRF():
	data = ""
	if request.remote_addr == POD_IP:
		if "flag" in request.url_rule.rule:
			webhook = request.args.get("webhook", "")
			if webhook:
				try:
					r = requests.post(webhook, data="{flag}".format(flag=FLAG))
					data = "all done. check your webhook captain, the flag is there.\n"
				except:
					return "give me a *valid* webhook\n", 500
			else:
				data = "pass me a webhook please\n"
		else:
			data = "go to /flag!!!\n"
	else:
		data = "i only get requests from the captain :/\n"

	return str(data)

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0', port=1337)