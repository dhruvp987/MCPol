import httpx


class HttpxClient:
    def __init__(self):
        self._client = httpx.AsyncClient()
        self._default_headers = {"Accepts": "application/json"}

    async def request(
        self, url: str, headers: dict[str, str] | None = None, timeout: float = 30.0
    ) -> dict[str, object]:
        if headers == None:
            headers = self._default_headers
        response = await self._client.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
        return response.json()
