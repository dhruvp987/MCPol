import os

CONGRESS_API_KEY_ENV = "MCPOL_CONGRESS_API_KEY"


class Config:
    def __init__(self):
        self.congress_api_key: str = os.getenv(CONGRESS_API_KEY_ENV, "")
        if self.congress_api_key == "":
            raise ValueError(
                f"Congress.gov API key is requried. Set it to the environment variable {CONGRESS_API_KEY_ENV}"
            )
