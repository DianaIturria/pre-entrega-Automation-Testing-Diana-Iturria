# Pre-Entrega: Automation Testing - Diana Iturria

## Propósito
Automatizar flujos básicos en https://www.saucedemo.com usando Selenium WebDriver, Python y Pytest.

El objetivo es automatizar los siguientes flujos en la aplicación SauceDemo:

- Login con credenciales válidas e inválidas
- Verificación del catálogo de productos
- Interacción con el carrito de compras (añadir productos y verificar su contenido)
- Cierre de sesión

## Tecnologías
- **Python** - Lenguaje de programación principal utilizado para escribir los tests y scripts de automatización.
- **Selenium WebDriver** - Para la automatización de la interfaz web
- **Chrome / ChromeDriver** - Navegador y driver necesario para ejecutar las pruebas automatizadas.
- **Pytest** - Framework de testing para estructurar y ejecutar pruebas
- **Pytest-html** - Permite generar reportes HTML con los resultados de las pruebas.
- **Git/GitHub** - Sistema de control de versiones y compartir el código.

## Instalar Dependencias
(Nota: en algunos sistemas como Mac, puede ser necesario usar pip3 en lugar de pip)

pip install pytest pytest-html selenium

Instalar ChromeDriver (solo en macOS):
brew install chromedriver

En Windows o Linux, se recomienda descargar ChromeDriver compatible con la versión de Chrome desde el sitio oficial o usar webdriver-manager en Python.

## Cómo ejecutar las pruebas
- Ejecutar todos los tests con reporte HTML:
```
pytest -v --html=reports/report.html --self-contained-html

- Ejecutar un test específico:
```
pytest tests/test_inventory.py -v

## Funcionalidades Implementadas

1.- **Automatización de Login Caso de éxito con credenciales válidas**
- Caso de fallo con credenciales inválidas

2.- **Verificación del Catálogo Comprobación del título de la página**
- Verificación de presencia de productos
- Validación de elementos de la interfaz (menú, filtros, etc.)

3.- **Interacción con el Carrito Añadir producto al carrito**
- Verificar que el contador se incremente
- Navegar al carrito
- Comprobar que el producto añadido aparezca correctamente

4.- **Cierre de Sesión Verificar que el usuario pueda cerrar sesión correctamente**

## Autor: **Diana Iturria**

## Notas 
Este proyecto fue desarrollado como pre-entrega para el curso de Automatización de Testing de Talento Tech. Todas las pruebas están diseñadas para funcionar con el sitio web SauceDemo en su versión actual.
