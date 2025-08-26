# spotify/middleware.py
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware:
    """
    Middleware to log each incoming request with method, path, and timestamp.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Before view is called
        method = request.method
        path = request.get_full_path()
        ip = self.get_client_ip(request)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        logger.info(f"[{timestamp}] {method} {path} from {ip}")

        response = self.get_response(request)

        # After view is called
        logger.info(f"[{timestamp}] Response status: {response.status_code} for {method} {path}")

        return response

    def get_client_ip(self, request):
        """Helper to fetch client IP address safely."""
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            return x_forwarded_for.split(",")[0]
        return request.META.get("REMOTE_ADDR")
