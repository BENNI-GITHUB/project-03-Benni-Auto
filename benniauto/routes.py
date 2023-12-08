from flask import render_template, request, redirect, url_for
from benniauto import app, db
from benniauto.models import Service, Order


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/add_service", methods=["GET","POST"])
def add_service():
    if request.method == "POST":
        service = Service(
            service_name=request.form.get("service_name"),
            image_url=request.form.get("image_url"),
            service_description=request.form.get("service_description")
        )
        db.session.add(service)
        db.session.commit()
        return redirect(url_for("services"))
    return render_template("add_service.html")

@app.route("/orders")
def orders():
    return render_template("orders.html")