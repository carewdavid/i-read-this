from flask import Flask, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return """<title>I Read This</title>
        <form method="POST" action="/add-article">
        <label for="url">Article url:</label>
        <input id="url" name="url" type="text">
        <input type="submit" value="submit">
        </form>"""
