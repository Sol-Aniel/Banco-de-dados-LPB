from flask import Flask,jsonify, render_template, Blueprint, redirect, url_for, request, flash, abort
from flask_sqlalchemy import SQLAlchemy
from database import db, init_db
from model import User, Product
from dao import userDAO
from repository.userrepository import UserRepository

sol_ = Blueprint('sol',__name__)
repositoriofoda = UserRepository()

@sol_.route ("/")
def index():
    return "Olá Banco de Dados"

@sol_.route ("/add")
def add():
    return repositoriofoda.add()

@sol_.route ("/see")
def see():
    return jsonify(repositoriofoda.query_json())