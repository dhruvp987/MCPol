import asyncio

from config import Config
from congressdata import CongressData
from httpxclient import HttpxClient


async def main():
    config = Config()
    http_client = HttpxClient()
    congress_client = CongressData(config.congress_api_key, http_client)
    bill_list = await congress_client.get_bill_list()
    print(bill_list)


if __name__ == "__main__":
    asyncio.run(main())
