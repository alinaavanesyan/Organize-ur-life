from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import random
'''from flask_migrate import Migrate'''
import datetime
from datetime import datetime

app = Flask(__name__) #создаём объект на основе класса Flask, передаём название основного файла (app.py)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
'''migrate = Migrate(app, db)'''


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    '''created_on = db.Column(db.DateTime(), default=datetime.now())'''
    text = db.Column(db.String(200), nullable=False)
    deadline = db.Column(db.DateTime())
    complete = db.Column(db.Boolean)


@app.route('/', methods=['POST', 'GET'])
def index():
    incomplete = Todo.query.filter_by(complete=False).all()
    complete = Todo.query.filter_by(complete=True).all()
    with open('templates/quotes.txt', encoding="UTF-8") as f:
        if request.method == 'GET':
            n = random.randint(0, 11)
            n *= 2
            k = 0
            for line in f:
                if k == n:
                    line1 = line
                elif k == n + 1:
                    return render_template('index.html', incomplete=incomplete, complete=complete, line1=line1, line=line)
                k += 1


@app.route('/add', methods=['POST'])
def add():
    if request.form['deadline'] != "":
        todo = Todo(text=request.form['todoitem'], deadline=datetime.strptime(request.form['deadline'], "%Y-%m-%d"), complete=False)
    else:
        todo = Todo(text=request.form['todoitem'], complete=False)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/complete/<id>')
def complete(id):
    todo = Todo.query.filter_by(id=int(id)).first()
    todo.complete = True
    db.session.commit()
    #остаемся на главной странице
    return redirect(url_for('index'))


@app.route('/incomplete/<id>')
def incomplete(id):
    todo = Todo.query.filter_by(id=int(id)).first()
    todo.complete = False
    db.session.commit()
    #остаемся на главной странице
    return redirect(url_for('index'))

@app.route('/delete/<id>')
def delete(id):
    todo = Todo.query.filter_by(id=int(id)).first()
    db.session.delete(todo)
    db.session.commit()
    #остаемся на главной странице
    return redirect(url_for('index'))

@app.route('/update/<id>', methods=['POST'])
def update(id):
    quer = Todo.query
    filtr = quer.filter_by(id=int(id))
    form_name = "todo_" + str(id)
    todo_text = request.form.get(form_name, "")
    filtr.update({"text": todo_text})
    db.session.commit()
    #остаемся на главной странице
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug = True) #потом надо будет сделать False
