import asyncio

from browser_use import Agent
from langchain_openai import ChatOpenAI

TASK = """
Googleで検索して男子プロテニスの香港オープンで錦織圭が今勝ち残っているかどうか教えてください。
""".strip()


async def main():
    agent = Agent(task=TASK, llm=ChatOpenAI(model="gpt-4o-mini"))
    result = await agent.run()
    print(result)


asyncio.run(main())
