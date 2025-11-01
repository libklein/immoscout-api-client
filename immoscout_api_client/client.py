"""ImmoScout24 API Client - Thin HTTP wrapper for the mobile API."""

from typing import Any

from rnet import Client, Impersonate

from immoscout_api_client.exceptions import ImmoscoutHTTPError
from immoscout_api_client.url_utils import get_expose_details_url, get_page_url


class ImmoscoutAPIClient:
    """
    A thin HTTP client for the ImmoScout24 mobile API.

    This client handles HTTP client setup and makes raw API requests,
    returning JSON responses as Python dictionaries. It does NOT handle
    retry logic, rate limiting, or response parsing - these are the
    responsibility of the caller.

    Args:
        timeout: HTTP request timeout in seconds (default: 30)
        impersonate: rnet impersonation mode (default: OkHttp5)
        user_agent: Custom user agent string (default: ImmoScout24 mobile app)
    """

    def __init__(
        self,
        timeout: int = 30,
        impersonate: Impersonate = Impersonate.OkHttp5,
        user_agent: str = "ImmoScout24_1410_30_._",
    ):
        self._client = Client(
            impersonate=impersonate,
            user_agent=user_agent,
            timeout=timeout,
        )

    async def search_list(self, mobile_url: str, page: int) -> dict[str, Any]:
        """
        Fetch a page of search results from the ImmoScout24 search API.

        Args:
            mobile_url: The mobile API URL (use convert_web_to_mobile to get this)
            page: Page number to fetch (1-indexed)

        Returns:
            Raw JSON response as a dictionary

        Raises:
            ImmoscoutHTTPError: If the HTTP request fails
        """
        page_url = get_page_url(mobile_url, page)

        try:
            response = await self._client.post(
                page_url,
                json={"supportedResultListType": [], "userData": {}},
            )
            return await response.json()
        except Exception as e:
            raise ImmoscoutHTTPError(
                status_code=getattr(e, "status_code", 0),
                message=f"Failed to fetch search results: {e}",
            ) from e

    async def get_property_details(self, listing_id: int) -> dict[str, Any]:
        """
        Fetch detailed information for a specific property listing.

        Args:
            listing_id: The property listing ID

        Returns:
            Raw JSON response as a dictionary

        Raises:
            ImmoscoutHTTPError: If the HTTP request fails
        """
        url = get_expose_details_url(listing_id)

        try:
            response = await self._client.get(url)
            return await response.json()
        except Exception as e:
            raise ImmoscoutHTTPError(
                status_code=getattr(e, "status_code", 0),
                message=f"Failed to fetch property details for listing {listing_id}: {e}",
            ) from e
