from flask import Flask, render_template
import random
import datetime as dt
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    return render_template(
        "index.html",
        num=random_number,
        current_year=dt.datetime.now().year,
        author="Hoang"
    )


@app.route('/guess/<name>')
def guess(name):
    gender = requests.get(f"https://api.genderize.io/?name={name}").json()["gender"]
    age = requests.get(f"https://api.agify.io/?name={name}").json()["age"]
    return render_template(
        "guess.html",
        name=name.capitalize(),
        gender=gender,
        age=age
    )


if __name__ == '__main__':
    app.run(debug=True)
