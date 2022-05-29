from datetime import datetime

from exts import db


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    username = db.Column(db.String(15),nullable=False)
    email = db.Column(db.String(20), nullable=False, unique=True)
    password =db.Column(db.String(100),nullable=False)
    role =db.Column(db.Enum('admin','njfUser','supplier'),default='supplier')
    rdatetime =db.Column(db.DateTime,default=datetime.now)

    def __str__(self):
        return self.username