from flask import (
    Blueprint, g, redirect, url_for, request, render_template
)
from app.db import get_db

bp = Blueprint('routes', __name__)

@bp.route("/")
def index():
    return render_template("base.html")

@bp.post("/add-article")
def add_article():
    url = request.form['url']
    print("\""+url+"\"")
    db = get_db()
    db.execute("INSERT INTO links (url) VALUES(?)", [url])
    db.commit()
    return redirect(url_for('routes.index'))

