from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def hello_world():
	today = datetime.today().strftime('%Y-%m-%d')
	return f'Hello MSOE friends and faculty. Today, {today} is going to be a good day!'

