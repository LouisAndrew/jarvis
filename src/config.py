from typing import TypedDict

from dotenv import dotenv_values


class Config(TypedDict):
    OPENAI_API_KEY: str


config: Config = dotenv_values(".env")
