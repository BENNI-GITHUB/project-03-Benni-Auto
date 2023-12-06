from benniauto import db
import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    password_confirmation = db.Column(db.String(255), nullable=False)
    # reviews = db.relationship("Review", backref="user_reviews", lazy=True)


class Service(db.Model):
    # schema for the Service model
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(25), unique=True, nullable=False)
    image_url = db.Column(db.String(2000), default='not-available.webp')
    orders = db.relationship("Order", backref="service", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.service_name



class Order(db.Model):
    # schema for the Order model
    id = db.Column(db.Integer, primary_key=True)
    user_car = db.Column(db.String(30), unique=True, nullable=False)
    order_title = db.Column(db.String(50), unique=True, nullable=False)
    order_description = db.Column(db.Text, nullable=False)
    request_date = db.Column(db.Date, nullable=False)
    need_recovery = db.Column(db.Boolean, default=False, nullable=False)
    user_postcode = db.Column(db.String(12), unique=True, nullable=False)
    user_address = db.Column(db.String(100), unique=True, nullable=False)
    user_phone = db.Column(db.String(12), unique=True, nullable=False) 
    service_id = db.Column(db.Integer, db.ForeignKey("service.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Order: {1} | Need Recovery: {2}".format(
            self.id, self.order_title, self.need_recovery
        )


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    # rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
    review_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    user = db.relationship("User", backref='reviews')
    service = db.relationship("Service", backref='reviews')













