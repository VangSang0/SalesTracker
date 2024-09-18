from flask import Flask, render_template, request, redirect, url_for, session


app = Flask(__name__)


@app.get('/')
def home():
    return render_template('index.html')



