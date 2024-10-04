from flask import Blueprint, render_template, request, jsonify
from .modules import socratist
import os
from . import limiter

views = Blueprint("views", __name__, url_prefix="/")

assistant_chatbot = socratist.Socratist(api_key=os.getenv("API_KEY"))

@views.route("/")
def index():
    return render_template("index.html")

@views.route("/ask", methods=["POST"])
@limiter.limit("4 per minute")
def ask_question():
    user_message = request.json['message']
    
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    response = assistant_chatbot.chat(user_message)
    
    return jsonify({"response": response["response"]})