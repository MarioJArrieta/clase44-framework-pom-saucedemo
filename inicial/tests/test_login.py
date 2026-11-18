"""Ejemplo: dos pruebas que ya usan el page object LoginPage. Imítalas."""
from playwright.sync_api import Page, expect

from datos import BLOQUEADO, ESTANDAR
from pages.login_page import LoginPage


def test_login_exitoso(page: Page):
    LoginPage(page).abrir().iniciar_sesion(ESTANDAR.nombre, ESTANDAR.clave)

    # TODO (taller): cuando exista InventarioPage, verifica su encabezado en vez de la URL.
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


def test_usuario_bloqueado_ve_mensaje(page: Page):
    login = LoginPage(page).abrir().intentar_iniciar_sesion(BLOQUEADO.nombre, BLOQUEADO.clave)

    expect(login.mensaje_error).to_contain_text("this user has been locked out")
