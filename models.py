from extensions import db
from datetime import datetime

class URL(db.Model):
    __tablename__ = 'urls'
    
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(2048), nullable=False)
    short_code = db.Column(db.String(10), unique=True, index=True) # Index is crucial for speed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, original_url):
        self.original_url = original_url