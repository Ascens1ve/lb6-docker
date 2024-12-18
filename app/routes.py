from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Store, Department, Product

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stores')
def stores():
    stores = Store.query.all()
    return render_template('store.html', stores=stores)

@app.route('/departments')
def departments():
    departments = Department.query.all()
    return render_template('departments.html', departments=departments)

@app.route('/products')
def products():
    products = Product.query.all()
    return render_template('products.html', products=products)

@app.route('/add_store', methods=['POST'])
def add_store():
    class_name = request.form['class']
    number = request.form['number']
    
    if class_name and number:
        new_store = Store(class_name=class_name, number=number)
        db.session.add(new_store)
        db.session.commit()
        
    return redirect(url_for('stores'))

@app.route('/add_department', methods=['POST'])
def add_department():
    name = request.form['name']
    manager = request.form['manager']
    store_id = request.form['store_id']
    
    if name and manager and store_id:
        new_department = Department(name=name, manager=manager, store_id=store_id)
        db.session.add(new_department)
        db.session.commit()

    return redirect(url_for('departments'))

@app.route('/add_product', methods=['POST'])
def add_product():
    name = request.form['name']
    price = request.form['price']
    sort = request.form['sort']
    quantity = request.form['quantity']
    department_id = request.form['department_id']
    
    if name and price and sort and quantity and department_id:
        new_product = Product(name=name, price=price, sort=sort,
                              quantity=quantity, department_id=department_id)
        db.session.add(new_product)
        db.session.commit()

    return redirect(url_for('products'))

