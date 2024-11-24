from flask import render_template, jsonify
from app import create_app

app = create_app()


@app.route('/')
def home():
    return jsonify({"message": "Welcome to the University Marketplace"})