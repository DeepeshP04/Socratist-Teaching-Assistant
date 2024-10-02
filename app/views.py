from flask import Blueprint, render_template, request, jsonify
from .modules import socraticlearn_ai
import os

views = Blueprint("views", __name__, url_prefix="/")

@views.route("/")
def index():
    return render_template("index.html")

@views.route("/ask", methods=["POST"])
def ask_question():
    socratic_ai = socraticlearn_ai.SocraticLearnAi(api_key=os.getenv("API_KEY"))

    data = request.get_json()
    print(data)
    user_message = data.get("message")
    chat_history = data.get("history", [])
    
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    
    response_data = socratic_ai.chat(user_message, chat_history)
    print(response_data)
    
    return jsonify(response_data)