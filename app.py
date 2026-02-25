from flask import Flask, render_template, request, jsonify
from chatbot_logic import get_chatbot_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot():
    user_input = request.form.get("msg")
    username = request.form.get("username")

    if not user_input:
        return jsonify({"response": "Please enter a valid message."})

    response = get_chatbot_response(user_input, username)

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
