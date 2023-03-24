import time
from collections import defaultdict, deque

class RateLimiter:
    def __init__(self, config):
        self.config = config or {}
        self.requests = defaultdict(deque)
        self.whitelisted_ips = set(self.config.get("whitelisted_ips", []))
        self.blacklisted_ips = set(self.config.get("blacklisted_ips", []))
        self.rate_limits = self.config.get("rate_limits", [{"time_window": 60, "max_requests": 2}])

    def is_limited(self, request):
        """Check if the request rate limit has been exceeded."""
        client_ip = request.remote_addr

        if client_ip in self.blacklisted_ips:
            return True

        if client_ip in self.whitelisted_ips or not self.config:
            return False

        current_time = time.time()
        for rate_limit in self.rate_limits:
            time_window = rate_limit["time_window"]
            max_requests = rate_limit["max_requests"]

            # Remove requests outside the current time window
            while self.requests[client_ip] and self.requests[client_ip][0] < current_time - time_window:
                self.requests[client_ip].popleft()

            # Check if the number of requests within the time window exceeds the limit
            if len(self.requests[client_ip]) >= max_requests:
                return True

            # Add the current request to the deque
            self.requests[client_ip].append(current_time)

        return False
