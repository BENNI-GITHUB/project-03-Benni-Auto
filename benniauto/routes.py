from flask import render_template, request, redirect, url_for, session, flash
from benniauto import app, db
from benniauto.models import Service, Order, User


@app.route("/")
def home():
    active = 'home'
    services = list(Service.query.order_by(Service.service_name).all())
    return render_template("home.html" , active=active, services=services )


@app.route("/register", methods=['GET', 'POST'])
def register():
    active = 'login'
    error = None
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        gender = request.form.get("gender")
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        password_confirmation = request.form.get("password_confirmation")

        # Check non-reiterativity of email
        user_email = User.query.filter_by(email=email).first()
        if user_email:
            flash('Error! User with this email is already registered', 'register')
            return render_template('register.html')

        # Check non-reiterativity of username
        user_username = User.query.filter_by(username=username).first()
        if user_username:
            flash('Error! Username already in use. Please Choose another one', 'register')
            return render_template('register.html')

        # Check Passwords similarity
        if password != password_confirmation:
            print("passwords are not same")
            flash('Error! Passwords are not same. Please try again', 'register')
            return render_template('register.html')


        user = User(
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            username=username, 
            email=email, 
            password=password, 
            password_confirmation=password_confirmation
        )

        db.session.add(user)
        db.session.commit()

        flash('Welcome to Benni Auto', 'login')
        return redirect('login')

    return render_template("register.html", active=active)


@app.route("/login", methods=['GET', 'POST'])
def login():
    active = 'login'
    users = list(User.query.order_by(User.username).all())
    if request.method == "POST":
        username = request.form.get('username')
        password_requested = request.form.get('password')
        print("login")
        user = User.query.filter_by(username=username).first()
        if user:
            user_password = user.password
            # login Successful 
            if user_password == password_requested:
                session['user_login'] = True
                session['user_fname'] = user.first_name
                session['user_id'] = user.id
                session['username'] = username
                print("login-session")
                return redirect(url_for('home'))
            else:
            # login Unsuccessful 
                flash('Password is not correct. Please try again.' , 'login')    
        else:
            flash('Error! Username is not found. Please try again.' , 'login')

    return render_template("login.html" , active=active, users=users)


@app.route("/logout")
def logout():
    session.clear()
    flash('You are logged out' , 'home')
    return redirect(url_for('home'))


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
            user_id = int(request.form.get("user_id"))
        )
        db.session.add(order)
        db.session.commit()
        return redirect(url_for("orders"))
    return render_template("add_order.html", services=services)


