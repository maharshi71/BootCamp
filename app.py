from flask import Flask, request, jsonify,render_template
from weather import weather

app = Flask(__name__)
db = {
    "Norman": weather("Norman", 89),
    "Oklahomacity": weather("Oklahomacity", 90),
    "Edmond": weather("Edmond", 99)
}


@app.route('/', methods = ["GET"])
def get_index():
    weather = [x.city for x in db.values()]
    return render_template('weather.html', len=len(weather), weather=weather)


@app.route('/api/weather', methods = ["GET", "POST"])
def get_weather():
    if request.method == "GET":
        city = request.args.get("city")
    else:
        city = request.get_json()["city"]
    weather = db[city]
    return jsonify(weather.__dict__)

@app.route('/weather/<city>')
def weather(city):
    weather = db[city]
    return render_template('index.html', city=weather.city, temp=weather.temp)



