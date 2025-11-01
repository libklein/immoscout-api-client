# immoscout-api-client

A thin Python client for the ImmoScout24 mobile API.

## Installation

```bash
pip install immoscout-api-client
```

Or with uv:

```bash
uv add immoscout-api-client
```

## Usage

### Basic Example

```python
import asyncio
from immoscout_api_client import ImmoscoutAPIClient, convert_web_to_mobile

async def main():
    # Initialize the client
    client = ImmoscoutAPIClient()

    # Convert a web URL to mobile API format
    web_url = "https://www.immobilienscout24.de/Suche/de/berlin/berlin/wohnung-mieten"
    mobile_url = convert_web_to_mobile(web_url)

    # Fetch first page of search results
    results = await client.search_list(mobile_url, page=1)
    print(f"Found {results['totalResults']} properties")

    # Get details for a specific property
    listing_id = results['resultListItems'][0]['item']['id']
    details = await client.get_property_details(listing_id)
    print(f"Property title: {details['sections'][0]['title']}")

asyncio.run(main())
```

## API Reference

### `ImmoscoutAPIClient`

Main HTTP client for the ImmoScout24 API.

**Constructor:**

```python
ImmoscoutAPIClient(
    timeout: int = 30,
    impersonate: Impersonate = Impersonate.OkHttp5,
    user_agent: str = "ImmoScout24_1410_30_._"
)
```

**Methods:**

- `async search_list(mobile_url: str, page: int) -> dict`
  - Fetch a page of search results
  - Returns raw JSON response

- `async get_property_details(listing_id: int) -> dict`
  - Fetch detailed information for a specific property
  - Returns raw JSON response

### URL Utilities

- `convert_web_to_mobile(web_url: str) -> str`
  - Convert web URL to mobile API format
  - Raises `ValueError` for invalid URLs or unsupported parameters

- `get_page_url(mobile_url: str, page: int) -> str`
  - Add/update page number in mobile API URL

- `get_expose_details_url(listing_id: int | str) -> str`
  - Construct property details endpoint URL

### Exceptions

- `ImmoscoutAPIError`: Base exception for all API errors
- `ImmoscoutHTTPError`: Raised when HTTP requests fail

## License

MIT License - see LICENSE file for details
