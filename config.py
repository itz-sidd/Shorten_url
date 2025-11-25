import os

class Config:
    # Default to localhost, but allow Docker to override via environment variables
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://user:password@localhost/url_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Redis URL
    REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379/0')