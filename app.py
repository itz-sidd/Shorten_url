# from flask import Flask
# from extensions import db, redis_client
# from routes import shortener_bp
# import os

# def create_app():
#     app = Flask(__name__)
    
#     # Configuration
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/url_db'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#     db_url = os.environ.get('DATABASE_URL', 'postgresql://user:password@localhost/url_db')
#     app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    
#     redis_url = os.environ.get('REDIS_URL', 'redis://localhost:6379/0')
#     app.config['REDIS_URL'] = redis_url 
    
#     # Update the redis_client init to use this URL
    
#     # Initialize Extensions
#     db.init_app(app)
#     redis_client.init_app(app) # Requires flask-redis

#     # Register Blueprints
#     app.register_blueprint(shortener_bp)
    
#     with app.app_context():
#         db.create_all() # Creates tables if they don't exist
        
#     return app

# if __name__ == '__main__':
#     app = create_app()
#     app.run(debug=True)

from flask import Flask
from config import Config          # <--- This imports your settings
from extensions import db, redis_client
from routes import shortener_bp

def create_app():
    app = Flask(__name__)
    
    # This ONE line loads all your database and redis URLs from config.py
    app.config.from_object(Config)
    
    # Initialize Plugins
    db.init_app(app)
    redis_client.init_app(app)

    # Register Blueprints
    app.register_blueprint(shortener_bp)
    
    # Create Database Tables
    with app.app_context():
        db.create_all()
        
    return app

if __name__ == '__main__':
    # usage: docker-compose up will run this
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    # app = create_app()
    # app.run(host='0.0.0.0', port=5000, debug=True)