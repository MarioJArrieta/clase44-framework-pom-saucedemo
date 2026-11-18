"""Datos de prueba de SauceDemo (públicos, los publica el propio sitio)."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Usuario:
    nombre: str
    clave: str = "secret_sauce"


@dataclass(frozen=True)
class Comprador:
    nombre: str
    apellido: str
    codigo_postal: str


ESTANDAR = Usuario("standard_user")
BLOQUEADO = Usuario("locked_out_user")
CON_PROBLEMAS = Usuario("problem_user")
LENTO = Usuario("performance_glitch_user")

COMPRADOR = Comprador("Ana", "Pérez", "230001")
