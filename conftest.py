import pytest

@pytest.fixture(scope="class")
def browser_context(playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=1000, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    yield context
    context.close()
    browser.close()

@pytest.fixture(scope="class")
def page(browser_context, base_url):
    page = browser_context.new_page()
    page.goto(base_url)
    yield page
    page.close()
