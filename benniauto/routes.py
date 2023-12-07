from flask import render_template
from benniauto import app, db


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/orders")
def orders():
    return render_template("orders.html")