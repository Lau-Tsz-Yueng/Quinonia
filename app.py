from flask import Flask, render_template, request, redirect, url_for, g
import sqlite3
import atexit
import os


def create_app():
    app = Flask(__name__)
    DATABASE = 'forum.db'

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS posts
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT NOT NULL,
                   content TEXT NOT NULL)''')

    @app.teardown_appcontext
    def close_connection(exception):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            title = request.form['title']
            content = request.form['content']
            with sqlite3.connect(DATABASE) as conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
                conn.commit()

        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM posts')
            posts = cursor.fetchall()

        return render_template('index.html', posts=posts)

    @app.route('/add_post', methods=['POST'])
    def add_post():
        title = request.form['title']
        content = request.form['content']
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
            conn.commit()
        return redirect(url_for('index'))

    @app.route('/new_page')
    def new_page():
        return render_template('new_page.html')


    def cleanup_database():
        if os.path.exists(DATABASE):
            os.remove(DATABASE)

    atexit.register(cleanup_database)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
