import re
import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="function", autouse=True)
def before_each(page: Page):

    print("before each")
    page.goto("https://playwright.dev/")
    yield

def test(page: Page):
    
    expect(page).to_have_url("https://playwright.dev/")