import time
from collections import defaultdict

class RateLimiter:
    def __init__(self, config):
        self.config = config or {}
        self.requests = defaultdict(int)
        self.timestamps = defaultdict(float)

    def is_limited(self, request):
        """Check if the request rate limit has been exceeded."""
        if not self.config:
            return False

        client_ip = request.remote_addr
        self.requests[client_ip] += 1
        current_time = time.time()

        if self.timestamps[client_ip] == 0:
            self.timestamps[client_ip] = current_time

        time_elapsed = current_time - self.timestamps[client_ip]

        if time_elapsed > self.config.get("time_window", 60):
            self.timestamps[client_ip] = current_time
            self.requests[client_ip] = 1

        return self.requests[client_ip] > self.config.get("max_requests", 30)
