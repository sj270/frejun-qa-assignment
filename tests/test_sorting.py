def test_sort_items(page):
    # Login first
    page.fill('#user-name', 'standard_user')
    page.fill('#password', 'secret_sauce')
    page.click('#login-button')
    page.select_option('.product_sort_container', 'hilo')  # Price high to low
    assert "inventory.html" in page.url
