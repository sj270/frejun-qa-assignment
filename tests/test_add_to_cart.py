def test_add_to_cart_and_validate_total(page):
    page.fill('#user-name', 'standard_user')
    page.fill('#password', 'secret_sauce')
    page.click('#login-button')

    # Add two items
    page.click('text=Add to cart', nth=0)
    page.click('text=Add to cart', nth=1)
    page.click('.shopping_cart_link')

    # Assert 2 items are in cart
    assert page.locator('.cart_item').count() == 2
