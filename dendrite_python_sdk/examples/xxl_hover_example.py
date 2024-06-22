import os
import asyncio

from dendrite_python_sdk import DendriteBrowser
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


async def main(username: str):
    dendrite_browser = DendriteBrowser(
        dendrite_api_key=os.environ.get("DENDRITE_API_KEY", ""),
        openai_api_key=os.environ.get("OPENAI_API_KEY", "")
    )

    page = await dendrite_browser.goto(
        "https://www.xxl.se", scroll_through_entire_page=False
    )

    # Get elements with prompts instead of using brittle selectors
    menu_field = await page.get_interactable_element("Jakt and Outdoor")
    await menu_field.hover()

    print("DONE")
    await asyncio.sleep(20)



asyncio.run(main("coffecup25"))
