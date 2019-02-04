import os
from flask import Flask, render_template
from pymongo import MongoClient

APP = Flask(__name__)

CLIENT = MongoClient(
    os.environ['DB_PORT_27017_TCP_ADDR'],
    27017)

DB = CLIENT.clang_warnings


@APP.route('/')
def main():
    # items = DB.clang_warnings.find()
    # items = [item for item in _items]

    return render_template('home.html')


@APP.route('/about')
def about():
    return render_template('about.html')


@APP.route('/checks')
def checks():
    return render_template('checks.html')


if __name__ == "__main__":
    APP.run(host='0.0.0.0', debug=True)
