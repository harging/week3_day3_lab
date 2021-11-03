from flask import Flask

shop = Flask(__name__)

from controllers import controller

if __name__ == '__main__':
    shop.run(debug=True)