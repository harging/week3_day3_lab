from flask import render_template
from app import app
from models.orders import orders_list

@app.route('/')
def home():
    return f"Welcome to SHOP!"

@app.route('/orders')
def list_orders():
    return render_template('index.html', title='Orders', myorders=orders_list)

@app.route('/orders/<index>')
def one_order(index):
    return render_template('order.html', title='Order', myorders=orders_list[int(index)])