from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('index.html')

@app.route("/contact")
def about():
	return render_template('contact.html')

car = {"car_id": "112093012309120310", "car_model": "Honda", "car_speed": "200"}

@app.route("/data")
def data():
	return render_template("data.html", car=car)

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)
