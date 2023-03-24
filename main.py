from bot_defender import BotDefender, load_config
import requests  # You may need to install this library: pip install requests

config = load_config("config.json")
bot_defender = BotDefender(config)

def handle_request(request):
    if bot_defender.check_request(request):
        print("Request allowed (not a bot).")
        # Process the request
    else:
        print("Request rejected (bot detected).")
        # Reject the request

# Simulate a request to your application
fake_request = requests.get("https://example.com")
handle_request(fake_request)
