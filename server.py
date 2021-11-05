from flask import Flask, render_template, redirect, request

# import the class from user.py
from user import User


app = Flask(__name__)
app.secret_key = "keep it secret, keep calm and code on"


@app.route("/")
def index():
    # call the get all classmethod to get all users
    users = User.get_all()
    return render_template("index.html", all_users = users)


@app.route("/users/new")
def new_user():
    return render_template("new_user.html")


@app.route("/users/create", methods = ["POST"])
def create_user():
    User.create(request.form)

    return redirect("/")






if __name__ == "__main__":
    app.run(debug = True)