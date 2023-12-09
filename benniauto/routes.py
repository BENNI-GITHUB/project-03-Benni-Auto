from flask import render_template, request, redirect, url_for, session, flash
from benniauto import app, db
from benniauto.models import Service, Order, User


@app.route("/")
def home():
    active = 'home'
    services = list(Service.query.order_by(Service.service_name).all())
    return render_template("home.html" , active=active, services=services )


@app.route("/login")
def login():
    active = 'login'
    return render_template("login.html" , active=active)


@app.route("/register")
def register():
    active = 'login'
    return render_template("register.html", active=active)


@app.route("/services")
def services():
    active = 'services'
    services = list(Service.query.order_by(Service.service_name).all())
    return render_template("services.html" , services=services , active=active)


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


@app.route("/edit_service/<int:service_id>", methods=["GET","POST"])
def edit_service(service_id):
    service = Service.query.get_or_404(service_id)
    if request.method == "POST":
        service.service_name = request.form.get("service_name")
        service.image_url = request.form.get("image_url")
        service.service_description = request.form.get("service_description")
        db.session.commit()
        return redirect(url_for("services"))
    return render_template("edit_service.html", service=service)


@app.route("/delete_service/<int:service_id>")
def delete_service(service_id):
    service = Service.query.get_or_404(service_id)
    db.session.delete(service)
    db.session.commit()
    return redirect(url_for("services"))


@app.route("/orders")
def orders():
    orders = list(Order.query.order_by(Order.id).all())
    return render_template("orders.html" , orders=orders)


@app.route("/add_order", methods=["GET", "POST"])
def add_order():
    services = list(Service.query.order_by(Service.service_name).all())
    if request.method == "POST":
        order = Order(
            order_title = request.form.get("order_title"),
            car_type = request.form.get("car_type"),
            order_description = request.form.get("order_description"),
            request_date = request.form.get("request_date"), 
            need_recovery = bool(True if request.form.get("need_recovery") else False),
            user_postcode = request.form.get("user_postcode"),
            user_address = request.form.get("user_address"),
            user_phone = request.form.get("user_phone"),
            service_id = request.form.get("service_id"),
            user_id = request.form.get("user_id")
        )
        db.session.add(order)
        db.session.commit()
        return redirect(url_for("orders"))
    return render_template("add_order.html", services=services)


