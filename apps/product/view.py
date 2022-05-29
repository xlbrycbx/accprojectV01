import xlrd as xlrd
from flask import Blueprint, request, render_template, jsonify, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

from apps.product.models import Product, Product_supplier, Supplier
from apps.user.models import User
from exts import db

product_bp = Blueprint('product', __name__, url_prefix='/product')


@product_bp.route('/', methods=['GET', 'POST'])
def product():
    msg = ''
    if request.method == 'POST':
        file = request.files.get('file')
        f = file.read()
        clinic_file = xlrd.open_workbook(file_contents=f)
        table = clinic_file.sheet_by_index(0)
        nrows = table.nrows
        print(nrows)
        for i in range(1, nrows):
            row_data = table.row_values(i)
            itemCode = str(int(row_data[0]))
            modelCode = str(int(row_data[1]))
            modelLable = str(row_data[2])

            if Product.query.filter(Product.itemCode == itemCode).all():
                msg = '产品已存在'
                continue
            else:
                product = Product()
                product.itemCode = itemCode
                product.modelCode = modelCode
                product.modelLable = modelLable

                db.session.add(product)
                db.session.commit()
        products = Product.query.all()
        return render_template('product.html', products=products, msg=msg)
    else:
        products = Product.query.all()
        return render_template('product.html', products=products, msg=msg)


# def product():
#     msg = ''
#     if request.method == 'POST':
#
#         file = request.files.get('file')
#         print('hhhh')
#         f = file.read()
#         clinic_file = xlrd.open_workbook(file_contents=f)
#         # sheet1
#         table = clinic_file.sheet_by_index(0)
#         print('****************fuck!')
#
#         nrows = table.nrows
#
#         print('*******************************************')
#         print(nrows)
#         print("***********************************************")
#         for i in range(2, nrows + 1):
#             row_data = table.row_values(i)
#             itemCode = str(int(row_data[0]))
#             modelCode = str(int(row_data[1]))
#             modelLable = row_data[2]
#             supplierCode = str(int(row_data[3]))
#             if Product.query.filter(Product.itemCode == itemCode).all():
#                 if Product_supplier.query.filter(Product_supplier.supplierCode == supplierCode).all():
#                     msg = '此记录已存在'
#                     continue
#                 elif not Supplier.query.filter(Supplier.supplierCode == supplierCode).all():
#                     msg = '供应商不存在，请先维护供应商信息'
#                 else:
#                     product_supplier = Product_supplier
#                     product_supplier.itemCode = itemCode
#                     product_supplier.supplierCode = supplierCode
#                     db.session.add(product_supplier)
#                     db.session.commit()
#                     # db.session.close()
#             else:
#                 product = Product()
#                 product.itemCode = itemCode
#                 product.modelCode = modelCode
#                 product.modelLable = modelLable
#                 db.session.add(product)
#                 db.session.commit()
#                 product_supplier = Product_supplier
#                 product_supplier.itemCode = itemCode
#                 product_supplier.supplierCode = supplierCode
#                 db.session.add(product_supplier)
#                 db.session.commit()
#                 # db.session.close()
#         products = Product.query.all()
#         # product_suppliers = Product_supplier.query.all()
#         return render_template('product.html',products=products,msg=msg)
#     # products = Product.query.all()
#     # print(products)
#     else:
#         return render_template('product.html')


@product_bp.route('/supplier', methods=['GET', 'POST'])
def supplier():
    msg = ''
    if request.method == 'POST':
        supplierCode = request.form.get('supplierCode')
        supplierName = request.form.get('supplierName')
        contactPerson = request.form.get('contactPerson')
        phone = request.form.get('phone')
        email = request.form.get('email')
        if Supplier.query.get(supplierCode):
            supplier = Supplier.query.get(supplierCode)
            if not supplier.isdelete:
                msg = f'供应商{supplierCode}已存在'
            else:
                supplier.isdelete=False
                supplier.supplierName = supplierName
                supplier.contactPerson = contactPerson
                supplier.phone = phone
                supplier.email = email
                db.session.commit()
            suppliers = Supplier.query.filter(Supplier.isdelete==False).all()
            return render_template('supplier.html',suppliers=suppliers,msg=msg)

        else:
            supplier = Supplier()
            supplier.supplierCode = supplierCode
            supplier.supplierName = supplierName
            supplier.contactPerson = contactPerson
            supplier.phone = phone
            supplier.email = email

            db.session.add(supplier)
            db.session.commit()



        return redirect(url_for('product.supplier'))

    else:
        suppliers = Supplier.query.filter(Supplier.isdelete==False)
        return render_template('supplier.html',suppliers=suppliers,msg=msg)

@product_bp.route('/update',methods=['POST','GET'])
def supplier_update():
    if request.method == 'POST':

        supplierCode = request.form.get('supplierCode')


        supplierName = request.form.get('supplierName')
        contactPerson = request.form.get('contactPerson')
        phone = request.form.get('phone')
        email = request.form.get('email')

        supplier = Supplier.query.get(supplierCode)
        supplier.supplierName = supplierName
        supplier.contactPerson = contactPerson
        supplier.phone = phone
        supplier.email = email
        db.session.commit()
        return redirect(url_for('product.supplier'))

    else:
        supplierCode = request.args.get('supplierCode')
        # supplier = Supplier.query.filter(Supplier.supplierCode==supplierCode).first()
        supplier = Supplier.query.get(supplierCode)


        return render_template('updatesupplier.html',supplier=supplier)

@product_bp.route('/delete')
def supplier_delete():


    supplierCode = request.args.get('supplierCode')


    supplier = Supplier.query.get(supplierCode)
    supplier.isdelete = True
    db.session.commit()
    return redirect(url_for('product.supplier'))

@product_bp.route('/product_supplier',methods=['POST','GET'])
def product_supplier():
    if request.method == 'POST':
        itemCode = request.form.get('itemCode')
        supplierCode = request.form.get('supplierCode')

        product_supplier=Product_supplier()
        product_supplier.itemCode = itemCode
        product_supplier.supplierCode = supplierCode
        db.session.add(product_supplier)
        db.session.commit()

    else:
        return render_template('product_supplier.html')

