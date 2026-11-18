"""Compra completa «grabada» a lo lineal: todos los pasos y localizadores en
la misma función. Funciona, pero cada prueba nueva copiaría estas líneas.
Tu tarea es convertirla en page objects y un flujo."""
from playwright.sync_api import Page, expect


def test_compra_lineal(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    page.click("#add-to-cart-sauce-labs-backpack")
    page.click("#add-to-cart-sauce-labs-bolt-t-shirt")
    page.click(".shopping_cart_link")
    page.click("#checkout")
    page.fill("#first-name", "Ana")
    page.fill("#last-name", "Pérez")
    page.fill("#postal-code", "230001")
    page.click("#continue")
    expect(page.locator(".summary_total_label")).to_have_text("Total: $49.66")
    page.click("#finish")
    expect(page.locator(".complete-header")).to_have_text("Thank you for your order!")
