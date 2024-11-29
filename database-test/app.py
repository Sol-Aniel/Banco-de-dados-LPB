from flask import Flask,jsonify, render_template, redirect, url_for, request, flash, abort
from flask_sqlalchemy import SQLAlchemy
from database import db, init_db
from model import User, Product
from controller import *

app = Flask(__name__)
init_db(app)

app.register_blueprint(sol_)

if __name__ == "__main__":
    app.run()
