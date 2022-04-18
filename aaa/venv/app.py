from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__) #создаём объект на основе класса Flask, передаём название основного файла (app.py)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///phrases.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Quotes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quote = db.Column(db.Text, nullable=False)
    nom = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Quotes %r>' % self.id

@app.route('/exit')
@app.route('/', methods=['POST', 'GET'])
def index():
    with open('templates/quotes.txt', encoding="UTF-8") as f:
        if request.method == 'GET':
            n = random.randint(0, 11)
            n *= 2
            k = 0
            for line in f:
                if k == n:
                    line1 = line
                elif k == n + 1:
                    return render_template('index.html', line1=line1, line=line)
                k += 1


if __name__ == '__main__':
    app.run(debug = True) #потом надо будет сделать False
