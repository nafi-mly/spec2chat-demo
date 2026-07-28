from flask import Flask, request, jsonify
from app.bot import KosanBot
import os

app = Flask(__name__)
bot = KosanBot()

@app.route("/webhook", methods=["POST"])
def webhook():
    """Webhook endpoint yang akan dipanggil oleh WhatsApp"""
    data = request.json
    
    user_id = data.get("from")  # WhatsApp user ID
    message = data.get("message", "")
    
    if not user_id or not message:
        return jsonify({"error": "Invalid request"}), 400
    
    # Process message
    response = bot.process_message(user_id, message)
    
    return jsonify({
        "to": user_id,
        "message": response
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)