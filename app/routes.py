from flask import (
    Blueprint, g, redirect, url_for, request, render_template
)
from app.db import get_db

bp = Blueprint('routes', __name__)

@bp.route("/")
def index():
    db = get_db()
    links = db.execute("SELECT url, added_at FROM links ORDER BY added_at DESC").fetchall()
    return render_template("base.html", links=links)

@bp.post("/add-article")
def add_article():
    url = request.form['url']
    print("\""+url+"\"")
    db = get_db()
    db.execute("INSERT INTO links (url) VALUES(?)", [url])
    db.commit()
    return redirect(url_for('routes.index'))

