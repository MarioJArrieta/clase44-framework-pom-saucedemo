"""Configuración común de la suite.

- Las páginas usan el atributo data-test de SauceDemo como test id.
- Tiempo máximo de espera de 10 s por acción.
- Si una prueba de interfaz falla, se toma una captura y se adjunta al
  reporte HTML (reportes/reporte.html).
"""
import base64

import pytest

TIMEOUT_MS = 10_000


@pytest.fixture(scope="session", autouse=True)
def configurar_test_id(playwright):
    # SauceDemo marca sus elementos con data-test="..."; así
    # page.get_by_test_id("login-button") encuentra data-test="login-button".
    playwright.selectors.set_test_id_attribute("data-test")


@pytest.fixture(autouse=True)
def tiempo_de_espera(request):
    # Solo aplica a las pruebas de interfaz (las que usan la fixture page).
    if "page" in request.fixturenames:
        request.getfixturevalue("page").set_default_timeout(TIMEOUT_MS)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    resultado = yield
    reporte = resultado.get_result()
    if reporte.when != "call" or not reporte.failed:
        return
    page = item.funcargs.get("page")
    if page is None:
        return
    try:
        import pytest_html
    except ImportError:
        return
    captura = base64.b64encode(page.screenshot(full_page=True)).decode()
    extras = getattr(reporte, "extras", [])
    extras.append(pytest_html.extras.png(captura, "Captura al fallar"))
    reporte.extras = extras


def pytest_html_report_title(report):
    report.title = "Clase #44 · Suite de SauceDemo con Page Object Model"
