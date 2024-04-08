from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/singnup")
def singnuo():
    return render_template("signup.html")
@app.route("/login")
def login():
    return render_template("login.html")
if __name__=="__main__":
    app.run(degub=True)
