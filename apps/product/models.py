from datetime import datetime



from exts import db


class Product(db.Model):
    itemCode = db.Column(db.String(7),primary_key=True)
    modelCode = db.Column(db.String(7),nullable=False)
    modelLable = db.Column(db.String(30), nullable=False)
    rdatetime =db.Column(db.DateTime,default=datetime.now)
    isdelete = db.Column(db.Boolean,default=False)
    suppliers = db.relationship('Product', backref='products',secondary='product_supplier')

    def __str__(self):
        return self.modelLable

class Supplier(db.Model):
    supplierCode = db.Column(db.String(10),primary_key=True)

    supplierName =db.Column(db.String(30),nullable=False)
    contactPerson = db.Column(db.String(10),nullable=False)
    phone = db.Column(db.String(11),nullable=False)
    email = db.Column(db.String(30), nullable=False)
    rdatetime =db.Column(db.DateTime,default=datetime.now)
    isdelete = db.Column(db.Boolean,default=False)


    def __str__(self):
        return self.supplierName

class Product_supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    supplierCode = db.Column(db.String(10),db.ForeignKey('supplier.supplierCode'),nullable =False)
    itemCode = db.Column(db.String(7),db.ForeignKey('product.itemCode'),nullable =False)
    supplier = db.relationship('Supplier',backref='product_suppliers')
    product = db.relationship('Product',backref='product_suppliers')