"""Pantalla de inicio de sesión de SauceDemo.

Reglas del page object (clase #44):
1. Métodos con la intención del usuario, no clics sueltos.
2. Cuando una acción navega, devuelve el page object de la pantalla siguiente.
3. Sin aserciones de negocio: expone el estado y la prueba decide.
4. Localizadores estables (data-test, rol o etiqueta), declarados solo aquí.
"""
from playwright.sync_api import Page

# TODO (taller): cuando crees pages/inventario_page.py, importa InventarioPage
# y haz que iniciar_sesion() la devuelva.


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.campo_usuario = page.get_by_test_id("username")
        self.campo_clave = page.get_by_test_id("password")
        self.boton_entrar = page.get_by_test_id("login-button")
        self.mensaje_error = page.get_by_test_id("error")

    def abrir(self) -> "LoginPage":
        self.page.goto("/")
        return self

    def iniciar_sesion(self, usuario: str, clave: str) -> Page:
        """Camino feliz: entra a la pantalla de productos.

        Por ahora devuelve la page de Playwright; en el taller la cambias para
        que devuelva InventarioPage(self.page).
        """
        self._enviar(usuario, clave)
        return self.page

    def intentar_iniciar_sesion(self, usuario: str, clave: str) -> "LoginPage":
        """Camino de error: se queda en esta pantalla para revisar el mensaje."""
        self._enviar(usuario, clave)
        return self

    def _enviar(self, usuario: str, clave: str) -> None:
        self.campo_usuario.fill(usuario)
        self.campo_clave.fill(clave)
        self.boton_entrar.click()
