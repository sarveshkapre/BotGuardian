from .rate_limiter import RateLimiter
from .captcha import Captcha
from .ip_analysis import IPAnalysis
from .user_agent_analysis import UserAgentAnalysis

class BotDefender:
    def __init__(self, config=None):
        self.config = config or {}
        self.init_components()

    def init_components(self):
        self.rate_limiter = RateLimiter(self.config.get("rate_limiter"))
        self.captcha = Captcha(self.config.get("captcha"))
        self.ip_analysis = IPAnalysis(self.config.get("ip_analysis"))
        self.user_agent_analysis = UserAgentAnalysis(self.config.get("user_agent_analysis"))

    def check_request(self, request):
        checks = [
            self.rate_limiter.is_limited(request),
            self.captcha.is_valid(request),
            self.ip_analysis.is_suspicious(request),
            self.user_agent_analysis.is_suspicious(request)
        ]

        return not any(checks)
