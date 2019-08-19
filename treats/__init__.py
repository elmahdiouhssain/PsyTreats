from datetime import datetime, timedelta
from flask import Flask, g, session, render_template, make_response
from flask_bootstrap import Bootstrap

app = Flask(__name__)


if __name__ == '__main__':
	#app.run()
  app.run(host='0.0.0.0', debug=True)