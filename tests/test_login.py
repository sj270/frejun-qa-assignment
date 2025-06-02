import pytest

def test_valid_login(page):
    page.fill('#user-name', 'standard_user')
    page.fill('#password', 'secret_sauce')
    page.click('#login-button')
    assert "inventory.html" in page.url

def test_invalid_login(page):
    page.fill('#user-name', 'invalid_user')
    page.fill('#password', 'wrong_pass')
    page.click('#login-button')
    assert page.locator('[data-test="error"]').is_visible()
