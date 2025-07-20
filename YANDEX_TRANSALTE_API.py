# YANDEX TRANSLATE API
from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright
import asyncio
import time

async def async_yandex_translate_api(text: str, from_lang: str, to_lang: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        async def block_unnecessary(route):
            if route.request.resource_type in ["image", "stylesheet", "font"]:
                await route.abort()
            else:
                await route.continue_()
        await page.route("**/*", block_unnecessary)
        await page.goto(f"https://translate.yandex.ru/?source_lang={from_lang}&target_lang={to_lang}&text={text}")

        timeout = 30
        start_time = time.time()
        translated = None
        while time.time() - start_time < timeout:
            await page.wait_for_timeout(200)  
            texts = await page.locator(".nI3G8IFy_0MnBmqtxi8Z").all_inner_texts()
            if texts and texts[0].strip():
                translated = texts[0]
                break
        if translated:
            await browser.close()
            return translated
        else:
            await browser.close()
            return "No text"

def yandex_translate_api(text: str, from_lang: str, to_lang: str) -> str:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        def block_unnecessary(route):
            if route.request.resource_type in ["image", "stylesheet", "font"]:
                route.abort()
            else:
                route.continue_()
        page.route("**/*", block_unnecessary)
        page.goto(f"https://translate.yandex.ru/?source_lang={from_lang}&target_lang={to_lang}&text={text}")

        timeout = 30  
        start_time = time.time()
        translated = None
        while time.time() - start_time < timeout:
            page.wait_for_timeout(200)  
            texts = page.locator(".nI3G8IFy_0MnBmqtxi8Z").all_inner_texts()
            if texts and texts[0].strip():
                translated = texts[0]
                break
        browser.close()
        if translated:
            return translated
        else:
            return "No text"