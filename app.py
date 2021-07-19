from flask import Flask, render_template
import random
import datetime as dt
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    return render_template(
        "index2.html",
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


@app.route('/blog/<num>')
def get_blog(num):
    blog_url = "https://api.npoint.io/706ae5b51a7218849686"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template(
        "blog.html",
        posts=all_posts,
        id=num
    )


if __name__ == '__main__':
    app.run(debug=True)
