from pydantic import BaseModel
from browser_use import Agent, Controller, ActionResult
from browser_use.browser.browser import Browser, BrowserConfig, BrowserContextConfig
from langchain_openai import ChatOpenAI
import asyncio
from typing import Optional
import json
import os
from dotenv import load_dotenv

load_dotenv()

class DoneResult(BaseModel):
    url: str
    summary: str
    topics: str

controller = Controller()

@controller.registry.action('Done executing task', param_model=DoneResult)
async def done(params: DoneResult) -> ActionResult:
    # Write the proposal as markdown with proper formatting
    markdown = f"""# Analysis

## URL
{params.url}

## Proposed Summary
{params.summary}

## Proposed Topics
{params.topics}
"""
    with open('analysis.md', 'w', encoding='utf-8') as f:
        f.write(markdown)

    return ActionResult(is_done=True, extracted_content=params.json())

async def main() -> None:
    agent = Agent(
        task=(
            "- Visit https://picoconsult.com/.\n"
            "- Find the 'About' section.\n"
            "- Analyze the main content of the 'About' section and\n"
            "  a) Write a concise, engaging summary (100-155 characters) that highlights the key themes and\n"
            "  b) Propose 5 relevant tags to categorize the content.\n"
        ),
        llm=ChatOpenAI(model="gpt-4"),
        controller=controller,
    )
    await agent.run(max_steps=50)

if __name__ == '__main__':
    asyncio.run(main())
