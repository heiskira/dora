from flask import request, jsonify
from .models import Product, Order, db

def create_product(data):
    new_product = Product(
        name=data['name'],
        price=data['price'],
        description=data.get('description', ''),
        stock=data.get('stock', 0)
    )
    db.session.add(new_product)
    db.session.commit()
    return new_product.to_dict()

def get_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products]), 200

def update_product(product_id):
    data = request.get_json()
    product = Product.query.get_or_404(product_id)
    product.name = data['name']
    product.price = data['price']
    product.description = data.get('description', product.description)
    product.stock = data.get('stock', product.stock)
    db.session.commit()
    return jsonify(product.to_dict()), 200

def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'}), 200

def create_order():
    data = request.get_json()
    new_order = Order(user_id=data['user_id'], product_id=data['product_id'], quantity=data['quantity'])
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'message': 'Order created successfully'}), 201

def get_orders():
    orders = Order.query.all()
    return jsonify([order.to_dict() for order in orders]), 200

def update_order(order_id):
    data = request.get_json()
    order = Order.query.get_or_404(order_id)
    order.quantity = data['quantity']
    db.session.commit()
    return jsonify({'message': 'Order updated successfully'}), 200

def delete_order(order_id):
    order = Order.query.get_or_404(order_id)
    db.session.delete(order)
    db.session.commit()
    return jsonify({'message': 'Order deleted successfully'}), 200