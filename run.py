from app import create_app, db
from app.models import User

app = create_app()

def add_default_user():
    with app.app_context():
        db.create_all()
        if User.query.filter_by(username='admin').first() is None:
            user = User(username='admin')
            user.set_password('password123')
            db.session.add(user)
            db.session.commit()

if __name__ == '__main__':
    add_default_user()
    app.run(debug=True)