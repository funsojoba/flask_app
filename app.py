from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Task %r>' % self.id

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        post_content = request.form['task']
        new_content = Todo(content=post_content)
        
        try:
            db.session.add(new_content)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'
    else:
        tasks = Todo.query.order_by(Todo.created_at).all()
        return render_template("index.html", tasks=tasks)
        
    

@app.route('/delete/<int:id>')
def delete(id):
    task = Todo.query.get_or_404(id)
    
    try:
        db.session.delete(task)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an error deleting your task'




if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='