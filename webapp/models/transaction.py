from webapp import db

from ..consts import TRANSACTION_TABLE_NAME

class Transaction(db.Model):
    __tablename__ = TRANSACTION_TABLE_NAME

    id = db.Column(db.Integer,unique=True, nullable=False, primary_key=True)
    date = db.Column(db.Date,nullable=False)
    vendor = db.Column(db.String,nullable=False)
    charge = db.Column(db.Float)
    credit = db.Column(db.Float)
    total_balance = db.Column(db.Float)
