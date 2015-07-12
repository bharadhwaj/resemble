from flask import Flask, request, render_template, url_for, redirect, flash, session, g, send_file, abort


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5050)
