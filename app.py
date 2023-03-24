from flask import Flask, request, jsonify
from bot_defender import BotDefender

app = Flask(__name__)

bot_defender = BotDefender({
    "user_agent_analysis": {
        "suspicious_user_agents": [
            "curl",
            "wget",
            "libwww-perl"
        ]
    }
})

@app.route("/")
def index():
    if bot_defender.check_request(request):
        return "Welcome to the website!"
    else:
        return "Access denied.", 403

if __name__ == "__main__":
    app.run(debug=True)
