from flask import Flask, request, render_template, url_for, redirect, flash, session, g, send_file, abort
import requests

import shutil

import requests


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template('index.html')
	if request.method == 'POST':
		app.logger.info("Fuck this shit")
		image1 = request.form['image1']
		image2 = request.form['image2']
		print image1, image2
		response = requests.get(image1, stream=True)
		with open('img1.png', 'wb') as out_file:
		    shutil.copyfileobj(response.raw, out_file)
		del response
		response = requests.get(image2, stream=True)
		with open('img2.png', 'wb') as out_file:
		    shutil.copyfileobj(response.raw, out_file)
		del response

		return render_template('index.html')





if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5050)
