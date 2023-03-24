class UserAgentAnalysis:
    def __init__(self, config):
        self.config = config or {}

    def is_suspicious(self, request):
        user_agent = request.headers.get("User-Agent", "").lower()
        suspicious_user_agents = self.config.get("suspicious_user_agents", [])

        for sus_ua in suspicious_user_agents:
            if sus_ua.lower() in user_agent:
                return True

        return False
