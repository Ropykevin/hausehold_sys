from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:Kevin254!@localhost:5432/mackaysdb"
db = SQLAlchemy(app)


class Households(db.Model):
    __tablename__ = 'households'
    id = db.Column(db.Integer, primary_key=True)
    house_number = db.Column(db.Integer, nullable=False)
    no_of_rooms = db.Column(db.Integer, nullable=False)
    rent = db.Column(db.String)
    tenants = db.relationship("Tenant", back_populates="household")

class Tenant(db.Model):
    __tablename__ = 'tenant'
    id = db.Column(db.Integer, primary_key=True)
    house_id = db.Column(db.Integer, db.ForeignKey('households.id'))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email_address = db.Column(db.String(255))
    contact = db.Column(db.String)
    payments = db.relationship("Payment", back_populates="tenant")
    household = db.relationship("Households", back_populates="tenants")


class Payment(db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenant.id'), nullable=False)
    payment_method = db.Column(db.String(255))
    amount_paid = db.Column(db.Numeric)
    tenant = db.relationship("Tenant", back_populates="payments")  # Adjusted to "Tenant"

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
