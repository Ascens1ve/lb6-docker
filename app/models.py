from app import db

class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(80), nullable=False)
    number = db.Column(db.String(20), nullable=False)
    departments = db.relationship('Department', backref='store', lazy=True)

    def __repr__(self):
        return f'<Store {self.class_name} - {self.number}>'

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    manager = db.Column(db.String(80), nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'), nullable=False)
    products = db.relationship('Product', backref='department', lazy=True)

    def __repr__(self):
        return f'<Department {self.name}>'

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    sort = db.Column(db.String(80), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'

