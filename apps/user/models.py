from datetime import datetime

from exts import db


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    username = db.Column(db.String(15),nullable=False)
    password =db.Column(db.String(32),nullable=False)
    role =db.Column(db.Enum('admin','njf','supplier'),default='supplier')
    rdatetime =db.Column(db.DateTime,default=datetime.now)

    def __str__(self):
        return self.username