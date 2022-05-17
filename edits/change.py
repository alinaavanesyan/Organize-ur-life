@app.route('/delete/<id>')
def delete(id):
    todo = Todo.query.filter_by(id=int(id)).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/update/<id>', methods=['POST'])
def update(id):
    quer = Todo.query
    filtr = quer.filter_by(id=int(id))
    form_name = "todo_" + str(id)
    todo_text = request.form.get(form_name, "")
    filtr.update({"text": todo_text})
    db.session.commit()
    return redirect(url_for('home'))
