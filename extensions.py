from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis

# Initialize them here, but don't bind to the app yet
db = SQLAlchemy()
redis_client = FlaskRedis()