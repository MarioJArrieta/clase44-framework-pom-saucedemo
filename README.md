# Kit del taller · Clase #44 · Framework con Page Object Model

Vas a construir un framework de automatización con **Page Object Model** y **Page Flow**
que corre contra un sitio público de práctica y genera un **reporte HTML**.

- **Sitio:** SauceDemo (Swag Labs) · https://www.saucedemo.com · usuarios `standard_user`,
  `locked_out_user`, `problem_user`, `performance_glitch_user`; clave `secret_sauce`.
- **Bonus API:** Restful-Booker · https://restful-booker.herokuapp.com
- **Herramientas:** Python 3.10 o superior, pytest, Playwright y pytest-html.

## 1. Instalación (hazla antes de la clase)

Para entregar tu trabajo en tu propio GitHub, crea tu copia con el botón verde
**Use this template → Create a new repository** y clona esa copia. Si solo quieres probar:

```bash
git clone https://github.com/MarioJArrieta/clase44-framework-pom-saucedemo.git
cd clase44-framework-pom-saucedemo
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium        # descarga el navegador (~150 MB)
```

## 2. Correr la suite

Se corre desde adentro de `inicial/`:

```bash
cd inicial
pytest                             # corre tests_lineal/ y tests/
pytest --headed --slowmo 300       # para ver el navegador mientras corre
```

El reporte queda en `inicial/reportes/reporte.html`: ábrelo con el navegador. Si una prueba
falla, el reporte trae la captura de pantalla del momento del fallo.

## 3. Qué trae `inicial/`

| Archivo | Qué es |
|---|---|
| `tests_lineal/test_compra_lineal.py` | Una compra completa «grabada»: todos los pasos y localizadores juntos. Pasa, pero no escala. |
| `pages/login_page.py` | Un page object **ya hecho**: el modelo a imitar. |
| `tests/test_login.py` | Dos pruebas que usan `LoginPage`. |
| `pages/components/`, `flows/` | Vacías: aquí va tu trabajo. |
| `datos.py` | Usuarios y comprador de prueba. |
| `conftest.py` | Configuración: `data-test` como test id, espera de 10 s y captura en fallos. |

## 4. Tu misión (55 minutos)

1. **(5 min)** Instala, corre `pytest` en `inicial/` y abre el reporte.
2. **(5 min)** Lee `pages/login_page.py` y `tests/test_login.py`.
3. **(25 min)** Construye el framework:
   - un page object por pantalla del flujo de compra: `InventarioPage`, `CarritoPage`,
     `CheckoutDatosPage`, `CheckoutResumenPage`, `CheckoutCompletoPage`;
   - el componente `Encabezado` (título, contador y enlace del carrito);
   - `flows/compra_flow.py` con `CompraFlow(page).comprar(productos)`;
   - al menos 5 pruebas: login exitoso, usuario bloqueado, agregar al carrito,
     ordenar por precio y compra completa con el flujo.
   - **Regla:** ningún localizador fuera de `pages/`.
4. **(10 min)** Corre toda la suite y abre el reporte. Haz fallar una prueba a propósito
   (por ejemplo, compra con `problem_user`) para ver la captura en el reporte.
5. **(10 min)** Socialización: comparte tu estructura de carpetas y tu reporte.

**Bonus:** una capa `api/` para Restful-Booker con 2 pruebas de API (usa
`playwright.request.new_context(base_url=...)`), o un segundo sitio público
(https://the-internet.herokuapp.com) con su propio page object.

## 5. Las 5 reglas del page object

1. Métodos con la intención del usuario (`iniciar_sesion`), no clics sueltos.
2. Si la acción navega, devuelve el page object de la pantalla siguiente.
3. Sin aserciones de negocio dentro del page object: la prueba decide.
4. Localizadores estables: `data-test` (`get_by_test_id`), rol o etiqueta antes que CSS o XPath.
5. Lo que se repite en varias pantallas (el encabezado) es un componente.

## 6. Entregable

Tu repositorio en GitHub (creado desde esta plantilla) con el framework, `reportes/reporte.html`, una captura del reporte
y un diagrama de capas (puede ser texto). Publica el enlace y la captura en el foro de la clase #44.

## Problemas frecuentes

- **`playwright: command not found`:** activa el entorno virtual antes de `playwright install`.
- **`ModuleNotFoundError: pages`:** corre `pytest` desde adentro de la carpeta (`inicial/`).
- **Fallas por tiempo:** son sitios públicos; si la red está lenta, vuelve a correr. `performance_glitch_user` es lento a propósito.
- **Restful-Booker** es compartida y se reinicia cada cierto tiempo: cada prueba crea sus propios datos.
