from benniauto import db
import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    password_confirmation = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return "Username: {0} , Email: {1}".format(
            self.username, self.email)


class Service(db.Model):
    # schema for the Service model
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(25), unique=True, nullable=False)
    image_url = db.Column(db.String(1000), default='no-image.jpg')
    service_description = db.Column(db.Text, nullable=True)
    orders = db.relationship("Order", backref="service", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.service_name





class Order(db.Model):
    # schema for the Order model
    id = db.Column(db.Integer, primary_key=True)
    order_title = db.Column(db.String(50), nullable=False)
    car_type = db.Column(db.String, nullable=False)
    order_description = db.Column(db.Text, nullable=False)
    request_date = db.Column(db.Date, nullable=False)
    need_recovery = db.Column(db.Boolean, default=False, nullable=False)
    user_postcode = db.Column(db.String(12), nullable=False)
    user_address = db.Column(db.String(80), nullable=False)
    user_phone = db.Column(db.String(12), nullable=False) 
    service_id = db.Column(db.Integer, db.ForeignKey("service.id", ondelete="CASCADE"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Order: {1} | Need Recovery: {2}".format(
            self.id, self.order_title, self.need_recovery
        )


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    rating = db.Column(db.String, nullable=False)
    comment = db.Column(db.Text)
    review_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)