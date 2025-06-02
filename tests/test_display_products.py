def test_display_products(page):
    page.fill('#user-name', 'standard_user')
    page.fill('#password', 'secret_sauce')
    page.click('#login-button')
    items = page.locator('.inventory_item')
    assert items.count() > 0
