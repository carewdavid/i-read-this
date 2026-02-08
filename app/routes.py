from flask import (
    Blueprint, g, redirect, url_for, request, render_template
)
import requests
from app.db import get_db

bp = Blueprint('routes', __name__)

@bp.route("/")
def index():
    db = get_db()
    links = db.execute("SELECT id, url, added_at FROM links ORDER BY added_at DESC").fetchall()
    return render_template("base.html", links=links)

@bp.post("/add-article")
def add_article():
    url = request.form['url']
    print("\""+url+"\"")
    db = get_db()
    db.execute("INSERT INTO links (url) VALUES(?)", [url])
    db.commit()
    return redirect(url_for('routes.index'))

@bp.get("/archive/<int:id>")
def archive_page(id):
        db = get_db()
        page = db.execute("SELECT content FROM pages WHERE id = ?", [id]).fetchone()
        if page is not None:
            return page['content']
        else:
            url = db.execute("SELECT url FROM links WHERE id = ?", [id]).fetchone()
            if url is None:
                abort(404)
            #Unpack url value from database row
            url = url['url']
            page = requests.get(url)
            db.execute("INSERT INTO pages (id, url, content) VALUES(?, ?, ?)", [id, url, page])
            db.commit()

                

