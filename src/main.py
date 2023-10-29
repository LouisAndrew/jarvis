#!/usr/bin/env python3

from config import config

from autogen import AssistantAgent, UserProxyAgent

task = """
write a summary of the content from the following file path: ./coding/output.txt
"""


def main():
    config_list = [
        {"model": "gpt-4", "api_key": config.get("OPENAI_API_KEY")},
        {"model": "gpt-3.5-turbo", "api_key": config.get("OPENAI_API_KEY")},
    ]

    assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})
    user_proxy = UserProxyAgent(
        "user_proxy", code_execution_config={"work_dir": "coding"}
    )
    user_proxy.initiate_chat(assistant, message=task)


main()
