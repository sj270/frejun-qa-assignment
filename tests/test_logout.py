def test_logout(page):
    page.fill('#user-name', 'standard_user')
    page.fill('#password', 'secret_sauce')
    page.click('#login-button')
    page.click('#react-burger-menu-btn')
    page.click('#logout_sidebar_link')
    assert "saucedemo.com" in page.url
