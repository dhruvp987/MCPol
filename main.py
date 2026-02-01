import asyncio

from config import Config
from congressdata import CongressData
from httpxclient import HttpxClient


async def main():
    config = Config()
    http_client = HttpxClient()
    congress_client = CongressData(config.congress_api_key, http_client)

    bill_list = await congress_client.get_bill_list()
    print(bill_list, end="\n\n")

    bill_overview = await congress_client.get_bill_overview(110, "hconres", 10)
    print(bill_overview, end="\n\n")

    bill_summaries = await congress_client.get_bill_summaries(110, "hconres", 10)
    print(bill_summaries, end="\n\n")

    bill_actions = await congress_client.get_bill_actions(110, "hconres", 10)
    print(bill_actions, end="\n\n")


if __name__ == "__main__":
    asyncio.run(main())
