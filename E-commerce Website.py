ecommerce_website/
│
├── app/
│   ├── static/
│   │   └── style.css
│   ├── templates/
│   │   ├── index.html
│   │   ├── product.html
│   │   └── cart.html
│   └── app.py
│
└── run.py






from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample product data
products = [
    {"id": 1, "name": "Laptop", "price": 800},
    {"id": 2, "name": "Smartphone", "price": 500},
    {"id": 3, "name": "Headphones", "price": 50},
]

cart = []

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product(product_id):
    product = next((item for item in products if item["id"] == product_id), None)
    return render_template('product.html', product=product)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    product = next((item for item in products if item["id"] == product_id), None)
    if product:
        cart.append(product)
    return redirect(url_for('index'))

@app.route('/cart')
def view_cart():
    return render_template('cart.html', cart=cart)

@app.route('/checkout')
def checkout():
    total_price = sum(item["price"] for item in cart)
    return f"Checkout successful! Total Price: ${total_price}"

if __name__ == '__main__':
    app.run(debug=True)






<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    <title>E-commerce Website</title>
</head>
<body>
    <h1>Products</h1>
    <ul>
        {% for product in products %}
            <li>
                <a href="{{ url_for('product', product_id=product['id']) }}">
                    {{ product['name'] }} - ${{ product['price'] }}
                </a>
                <a href="{{ url_for('add_to_cart', product_id=product['id']) }}">Add to Cart</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>






<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    <title>{{ product['name'] }}</title>
</head>
<body>
    <h1>{{ product['name'] }}</h1>
    <p>Price: ${{ product['price'] }}</p>
    <a href="{{ url_for('add_to_cart', product_id=product['id']) }}">Add to Cart</a>
</body>
</html>






<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    <title>Shopping Cart</title>
</head>
<body>
    <h1>Shopping Cart</h1>
    <ul>
        {% for item in cart %}
            <li>{{ item['name'] }} - ${{ item['price'] }}</li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('checkout') }}">Proceed to Checkout</a>
</body>
</html>






body {
    font-family: Arial, sans-serif;
    margin: 20px;
}

h1 {
    color: #333;
}

ul {
    list-style: none;
    padding: 0;
}

li {
    margin-bottom: 10px;
}

a {
    text-decoration: none;
    color: #007BFF;
    margin-left: 10px;
}
