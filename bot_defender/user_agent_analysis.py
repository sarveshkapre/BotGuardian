import re

class UserAgentAnalysis:
    def __init__(self, config):
        self.config = config or {}
        self.compile_patterns()

    def compile_patterns(self):
        """Pre-compile regular expressions for better performance."""
        suspicious_user_agents = self.config.get("suspicious_user_agents", [])
        self.allowed_user_agents = self.config.get("allowed_user_agents", [])
        self.patterns = [re.compile(sus_ua, re.IGNORECASE) for sus_ua in suspicious_user_agents]

    def is_suspicious(self, request):
        """Analyze the user agent string of the request and determine if it's suspicious."""
        user_agent = request.headers.get("User-Agent", "")

        # If allowed user agents are specified, check if the user agent matches any allowed user agent
        if self.allowed_user_agents:
            if not any(allowed_ua in user_agent for allowed_ua in self.allowed_user_agents):
                return True

        # Check if the user agent matches any suspicious user agent pattern
        for pattern in self.patterns:
            if pattern.search(user_agent):
                return True

        return False
