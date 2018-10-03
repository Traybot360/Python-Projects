from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/contact")
def about():
    return render_template('contact.html')

cars = [
    {"car_id": "112093012309120310", "car_model": "Honda",
     "car_speed": "200"},
    {"car_id": "212309120310093012", "car_model": "BMW",
     "car_speed": "180"},
    {"car_id": "312012031093012309", "car_model": "Subaru",
     "car_speed": "100"},
    {"car_id": "419120310209301230", "car_model": "Nisan",
     "car_speed": "200"},
    {"car_id": "509301230129120310", "car_model": "Toyota",
     "car_speed": "50"},
    {"car_id": "613091203102093012", "car_model": "Tesla",
     "car_speed": "210"},
    {"car_id": "712093003101230912", "car_model": "Acura",
     "car_speed": "20"},
    {"car_id": "801230120939120310", "car_model": "Lexus",
     "car_speed": "90"},
    {"car_id": "912093091203100123", "car_model": "Ford",
     "car_speed": "150"}
]

@app.route("/data")
def data():
    return render_template("data.html", cars=cars)

@app.route("/gallery")
def gallery():
    links = [
      "https://user-images.githubusercontent.com/16161226/46444401-df6b0500-c73f-11e8-89cb-ee3080c5080f.jpg",
      "https://user-images.githubusercontent.com/16161226/46444402-df6b0500-c73f-11e8-949a-e3e6675b11dd.jpg",
      "https://user-images.githubusercontent.com/16161226/46444403-df6b0500-c73f-11e8-8cba-5d664fc627fa.jpg",
      "https://user-images.githubusercontent.com/16161226/46444404-df6b0500-c73f-11e8-8c7f-44c8a8515d01.jpg"  
    ]

    return render_template("gallery.html", links=links)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
