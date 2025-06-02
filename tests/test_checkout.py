def test_checkout_process(page):
    page.fill('#user-name', 'standard_user')
    page.fill('#password', 'secret_sauce')
    page.click('#login-button')

    page.click('text=Add to cart', nth=0)
    page.click('.shopping_cart_link')
    page.click('#checkout')

    page.fill('#first-name', 'Sneha')
    page.fill('#last-name', 'Kumari')
    page.fill('#postal-code', '12345')
    page.click('#continue')

    assert page.locator('.summary_info').is_visible()
    page.click('#finish')
    assert "THANK YOU FOR YOUR ORDER" in page.text_content('.complete-header')
