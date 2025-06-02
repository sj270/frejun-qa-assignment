import pytest

@pytest.mark.parametrize("username,password", [
    ("locked_out_user", "secret_sauce"),
    ("standard_user", "wrong_pass"),
    ("", ""),
])
def test_invalid_login_combinations(page, username, password):
    page.fill('#user-name', username)
    page.fill('#password', password)
    page.click('#login-button')
    assert page.locator('[data-test="error"]').is_visible()
