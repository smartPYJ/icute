import os

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route ('/register')
def register():
    return render_template("register.html")


@app.route ('/contestants')
def contestant():
    return render_template("cuties.html")

@app.route ('/profile')
def profile():
    return render_template("profile.html")