from flask import Blueprint, jsonify, request, render_template, redirect, url_for, flash
from .controllers import create_product, get_products, update_product, delete_product

bp = Blueprint('routes', __name__)

@bp.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    product = create_product(data)
    return jsonify(product), 201

@bp.route('/products', methods=['GET'])
def list_products():
    products = get_products()
    return jsonify(products), 200

@bp.route('/products/<int:product_id>', methods=['PUT'])
def modify_product(product_id):
    data = request.get_json()
    product = update_product(product_id, data)
    return jsonify(product), 200

@bp.route('/products/<int:product_id>', methods=['DELETE'])
def remove_product(product_id):
    delete_product(product_id)
    return jsonify({'message': 'Product deleted'}), 204

@bp.route('/seller/add-product', methods=['GET', 'POST'])
def seller_add_product():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        price = request.form.get('price')
        description = request.form.get('description')
        stock = request.form.get('stock')

        # Validate form data
        if not name or not price or not stock:
            flash('Name, Price, and Stock are required fields!', 'error')
            return redirect(url_for('routes.seller_add_product'))

        try:
            # Create product
            product_data = {
                'name': name,
                'price': float(price),
                'description': description,
                'stock': int(stock)
            }
            create_product(product_data)
            flash('Product added successfully!', 'success')
            return redirect(url_for('routes.seller_add_product'))
        except Exception as e:
            flash(f'Error adding product: {str(e)}', 'error')

    return render_template('add_product.html')