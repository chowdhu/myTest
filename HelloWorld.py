from flask import Flask, render_template
import os,copy


app = Flask(__name__)


if os.getenv("VCAP_APP_PORT"):
	port = int(os.getenv("VCAP_APP_PORT"))
else:
	port = 8080

@app.route('/')
def render_page():
    return render_template('landing.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=port,debug=True)


