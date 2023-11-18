from mainApp import db
from datetime import datetime

class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sensor = db.Column(db.String(255), nullable=False)
    sensor_signal = db.Column(db.Boolean, nullable=False)
    sensor_value = db.Column(db.Float)
    save_date = db.Column(db.TIMESTAMP, default=datetime.utcnow)