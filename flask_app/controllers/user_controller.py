from flask import render_template, redirect, request
from werkzeug import datastructures

from flask_app import app
from flask_app.models.user import User


#READ MANY
@app.route("/")
def index():
    users = User.get_all()
    return render_template("index.html", all_users = users)


#CREATE - render new user form
@app.route("/users/new")
def new_user():
    return render_template("new_user.html")


#CREATE - POST
@app.route("/users/create", methods = ["POST"])
def create_user():
    User.create(request.form)

    return redirect("/")


#READ ONE
@app.route('/users/<int:user_id>')
def display_user(user_id):
    return render_template("single_user.html", user = User.get_one({'id': user_id}))


#UPDATE - render update form
@app.route('/users/<int:user_id>/edit_user')
def edit_user_form(user_id):
    return render_template('update_user.html', user = User.get_one({'id': user_id}))


#UPDATE - POST
@app.route('/users/<int:user_id>/update', methods = ['POST'])
def update_user(user_id):
    data = {
        **request.form,
        "id": user_id
    }
    User.update(data)

    return redirect(f"/users/{user_id}")


#DELETE
@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    User.delete({ 'id': user_id })
    
    return redirect('/')