from app import app, db
from models import User
from werkzeug.security import check_password_hash

with app.app_context():
    user = User.query.filter_by(username='gowrisankar').first()
    if user:
        print(f"User found: {user.username}")
        print(f"Email: {user.email}")
        print(f"Password hash: {user.password_hash}")
        print(f"Password check for 'pass': {check_password_hash(user.password_hash, 'pass')}")
    else:
        print("User not found!")
