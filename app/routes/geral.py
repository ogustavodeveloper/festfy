from flask import render_template, request, session, jsonify, redirect, make_response, Response
from app import db
from app.routes import geral_bp

@geral_bp.route("/")
def teste():
    return render_template("base.html")