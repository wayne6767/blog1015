
from flask import Flask, render_template, abort

app = Flask(__name__)

# 範例文章資料
posts = [
    {
        "id": 1,
        "title": "我的第一篇文章",
        "author": "小明",
        "content": "歡迎來到我的部落格！這是我的第一篇文章。"
    },
    {
        "id": 2,
        "title": "學習 Python Flask",
        "author": "小華",
        "content": "Flask 是一個輕量且容易上手的 Python Web 框架。"
    },
    {
        "id": 3,
        "title": "Templates 的使用方式",
        "author": "小美",
        "content": "我們可以透過 Jinja2 將 Python 資料傳遞到 HTML 頁面。"
    }
]


# 首頁：顯示所有文章
@app.route("/")
def index():
    return render_template("index.html", posts=posts)


# 文章詳細頁面，例如 /post/1
@app.route("/post/<int:post_id>")
def post_detail(post_id):
    post = next(
        (p for p in posts if p["id"] == post_id),
        None
    )

    if post is None:
        abort(404)

    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
