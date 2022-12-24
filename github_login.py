import re
import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="function", autouse=True)
def before_each(page: Page):

    print("before each")
    page.goto("https://github.com/login")
    yield


def test(page: Page):

    expect(page).to_have_url("https://github.com/login")
    page.wait_for_timeout(2000)
    page.get_by_label("Username or email address").fill("nonuser")
    page.get_by_label("Password").fill("1234")
    page.get_by_role("button", name="Sign in").click()
    page.wait_for_timeout(1000)
    isErrorMessage = page.get_by_text("Incorrect username or password.")

    expect(isErrorMessage).to_be_visible()
