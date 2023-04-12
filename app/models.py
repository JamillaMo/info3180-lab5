# Add any model classes for Flask-SQLAlchemy here
from . import db
import datetime
from sqlalchemy import Column, Integer, DateTime
from pytz import timezone

tz = timezone('EST')
#datetime.now(tz) 

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    description = db.Column(db.Text(255), unique=True)
    poster = db.Column(db.String(80), unique=True)
    created_at = Column(DateTime, default=datetime.datetime.now) #Check