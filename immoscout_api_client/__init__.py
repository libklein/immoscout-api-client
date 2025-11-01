"""ImmoScout24 API Client - A thin wrapper for the ImmoScout24 mobile API."""

from immoscout_api_client.client import ImmoscoutAPIClient
from immoscout_api_client.exceptions import ImmoscoutAPIError, ImmoscoutHTTPError
from immoscout_api_client.url_utils import convert_web_to_mobile, get_expose_details_url, get_page_url

__version__ = "0.1.0"

__all__ = [
    "ImmoscoutAPIClient",
    "ImmoscoutAPIError",
    "ImmoscoutHTTPError",
    "convert_web_to_mobile",
    "get_expose_details_url",
    "get_page_url",
]
