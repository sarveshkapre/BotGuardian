class Captcha:
    def __init__(self, config):
        self.config = config or {}

    def is_valid(self, request):
        """Check if the captcha response is valid."""
        if not self.config:
            return True

        captcha_response = request.form.get("captcha_response")

        if captcha_response:
            # Implement captcha validation logic here (e.g., with Google reCAPTCHA)
            return True

        return False
