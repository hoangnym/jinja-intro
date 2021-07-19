from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    all_posts = requests.get("https://api.npoint.io/706ae5b51a7218849686").json()
    print(all_posts)
    return render_template(
        "index.html",
        blog=all_posts
    )

@app.route('/blog/<num>')
def get_blog(num):
    return render_template(
        "post.html",
        num=num
    )

if __name__ == "__main__":
    app.run(debug=True)
