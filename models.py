from datetime import datetime
from cdk import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id): 
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(120), unique=False, nullable=False)
    first_name =  db.Column(db.String(120), unique=False, nullable=False)
    last_name =  db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    phone = db.Column(db.String(120), unique=False, nullable=False)
    address = db.Column(db.String(120), unique=False, nullable=False)
    ms = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return f"User('{self.role}', '{self.first_name}', '{self.last_name}', '{self.email}', \
        '{self.phone}', '{self.address}', '{self.ms}')"

    def __init__(self, role, first_name, last_name, email, password, phone, address, ms):
            self.first_name = first_name
            self.last_name = last_name
            self.password = password
            self.email = email
            self.phone = phone
            self.address = address
            self.ms = ms
            self.role = role

    def get_id(self):
            return self.id
    


#CREATE TABLE `Python_Employee` ( `id` INT NOT NULL , `name` TEXT NOT NULL , `photo` BLOB NOT NULL , `biodata` BLOB NOT NULL , PRIMARY KEY (`id`))
