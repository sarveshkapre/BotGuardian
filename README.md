# BotDefender

BotDefender is a Python library designed to protect web applications from bots and automated attacks. It provides a range of security features such as rate limiting, user agent analysis, IP analysis, and CAPTCHA validation.

## Features

Rate limiting: Limit the number of requests per IP address within a certain time window.
User agent analysis: Identify suspicious user agents and block requests from them.
IP analysis: Analyze and block IP addresses based on a set of configurable rules.
CAPTCHA validation: Verify user requests using CAPTCHA to prevent automated bots.

## Installation

Install the library using pip

```bash
pip install bot-defender
```

## Usage

Here's a basic example of how to use BotDefender with a Flask application:

```python
from flask import Flask, request, jsonify
from bot_defender import BotDefender

app = Flask(__name__)

config = {
    "rate_limiter": {
        "time_window": 60,
        "max_requests": 2,
    },
    "user_agent_analysis": {
        "allowed_user_agents": ["Mozilla/5.0", "Opera/9.80"],
        "suspicious_user_agents": ["curl", "wget", "Python-urllib"],
    },
    # Add other configuration options as needed
}

bot_defender = BotDefender(config)

@app.before_request
def before_request():
    if bot_defender.check_request(request):
        return jsonify({"error": "Access denied"}), 403

@app.route("/")
def home():
    return "Hello, World!"

if __name__ == "__main__":
    app.run()
```

## Configuration

BotDefender uses a configuration dictionary to customize its behavior. The following keys can be used:


`rate_limiter`: Rate limiting settings.

`time_window`: The time window in seconds during which requests are counted.
`max_requests`: The maximum number of requests allowed within the time window.
`user_agent_analysis`: User agent analysis settings.

`allowed_user_agents`: A list of allowed user agent substrings.
`suspicious_user_agents`: A list of suspicious user agent substrings.
`ip_analysis`: IP analysis settings.

`whitelist`: A list of whitelisted IP addresses.
`blacklist`: A list of blacklisted IP addresses.
`captcha`: CAPTCHA settings.

`site_key`: Your site key for the CAPTCHA service.
`secret_key`: Your secret key for the CAPTCHA service.

## Contributing

- Fork the repository on GitHub.
- Clone the forked repository to your local machine.
- Create a new branch for your changes.
- Make your changes and commit them to your branch.
- Push your changes to your forked repository.
- Open a pull request to merge your changes into the main repository.

## License

This project is licensed under the MIT License. See the LICENSE file for details.