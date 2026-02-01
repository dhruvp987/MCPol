from httpxclient import HttpxClient

CONGRESS_API_BASE_URL = "https://api.congress.gov/v3"
BILL_ENDPOINT = CONGRESS_API_BASE_URL + "/bill"


def _build_bill_overview_endpoint(
    congress_num: int, bill_type: str, bill_num: int
) -> str:
    return f"{BILL_ENDPOINT}/{congress_num}/{bill_type}/{bill_num}"


def _build_bill_actions_endpoint(
    congress_num: int, bill_type: str, bill_num: int
) -> str:
    return f"{BILL_ENDPOINT}/{congress_num}/{bill_type}/{bill_num}/actions"


class CongressData:
    def __init__(self, api_key: str, httpClient: HttpxClient):
        self._headers = {"x-api-key": api_key, "Accpet": "application/json"}
        self._client = httpClient

    async def get_bill_list(self) -> dict[str, object]:
        response = await self._client.request(BILL_ENDPOINT, self._headers)
        return response

    async def get_bill_overview(
        self, congress_num: int, bill_type: str, bill_num: int
    ) -> dict[str, object]:
        bill_overview_endpoint = _build_bill_overview_endpoint(
            congress_num, bill_type, bill_num
        )
        response = await self._client.request(bill_overview_endpoint, self._headers)
        return response

    async def get_bill_actions(
        self, congress_num: int, bill_type: str, bill_num: int
    ) -> dict[str, object]:
        bill_actions_endpoint = _build_bill_actions_endpoint(
            congress_num, bill_type, bill_num
        )
        response = await self._client.request(bill_actions_endpoint, self._headers)
        return response
