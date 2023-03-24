from flask import Flask, request, jsonify
from bot_defender import BotDefender

email_config = {
    "smtp_server": "smtp.example.com",
    "smtp_port": 465,
    "sender_email": "noreply@example.com",
    "email_password": "your_email_password",
}

email_client = EmailClient(email_config)

config = {"allowed_user_agents": ["Mozilla/5.0", "Opera/9.80"],
    "suspicious_user_agents": ["curl", "wget", "Python-urllib"],
    "rate_limits": [
        {"time_window": 60, "max_requests": 10},
        {"time_window": 3600, "max_requests": 100}
    ],
    "whitelisted_ips": ["192.0.2.1"],
    "blacklisted_ips": ["198.51.100.1"]
}

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
