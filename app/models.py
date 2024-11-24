from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # define additional fields


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # define additional fields


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # additional fields
