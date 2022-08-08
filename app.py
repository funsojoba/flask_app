from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config('SQLALCHEMY_DATABASE_URI', 'sqlite:///test.db')
db = SQLAlchemy(app)





@app.route('/')
def index():
    context ={
        "title":"Home base",
        "message":"comerade are we still together?"
    }
    return render_template("index.html", **context)




if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='