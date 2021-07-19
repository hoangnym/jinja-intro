from flask import Flask, render_template
import requests

all_posts = requests.get("https://api.npoint.io/706ae5b51a7218849686").json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template(
        "index.html",
        blog=all_posts
    )


@app.route('/post/<num>')
def get_blog(num):
    return render_template(
        "post.html",
        num=num,
        blog=all_posts[int(num)]
    )


if __name__ == "__main__":
    app.run(debug=True)
