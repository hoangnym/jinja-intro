from flask import Flask, render_template
from post import Post
import requests

posts = requests.get("https://api.npoint.io/706ae5b51a7218849686").json()
post_objects = [Post(post["id"], post["title"], post["subtitle"], post["body"]) for post in posts]

app = Flask(__name__)


@app.route('/')
def home():
    return render_template(
        "index.html",
        blog=post_objects
    )


@app.route('/post/<num>')
def get_blog(num):
    return render_template(
        "post.html",
        num=num,
        blog=post_objects[int(num)]
    )


if __name__ == "__main__":
    app.run(debug=True)
