from httpxclient import HttpxClient

CONGRESS_API_BASE_URL = "https://api.congress.gov/v3"
BILL_ENDPOINT = CONGRESS_API_BASE_URL + "/bill?format=json"


class CongressData:
    def __init__(self, api_key: str, httpClient: HttpxClient):
        self._headers = {"x-api-key": api_key, "Accpet": "application/json"}
        self._client = httpClient

    async def get_bill_list(self) -> dict[str, object]:
        response = await self._client.request(BILL_ENDPOINT, self._headers)
        return response
