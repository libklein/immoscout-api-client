"""Exceptions for the ImmoScout24 API client."""


class ImmoscoutAPIError(Exception):
    """Base exception for all ImmoScout API errors."""

    pass


class ImmoscoutHTTPError(ImmoscoutAPIError):
    """Exception raised when an HTTP error occurs."""

    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
        super().__init__(f"HTTP {status_code}: {message}")
