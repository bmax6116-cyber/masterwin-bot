from flask import Flask, request
import requests
import os

TOKEN = os.environ.get("BOT_TOKEN")
API_URL = f"https://api.telegram.org/bot{TOKEN}"

app = Flask(__name__)

@app.route("/")
def home():
    return "OK"

@app.route("/telegram/webhook", methods=["POST"])
def webhook():
    update = request.json

    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"].get("text", "")

        requests.post(f"{API_URL}/sendMessage", json={
            "chat_id": chat_id,
            "text": f"Hai scritto: {text}"
        })

    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

  
