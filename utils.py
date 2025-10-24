"""
Función para automatizar el login en la página de Saucedemo.

Parámetros:
driver : objeto WebDriver de Selenium, ya inicializado.

Pasos:
1. Navega a la URL de login.
2. Completa los campos de usuario y contraseña.
3. Hace clic en el botón de login.
4. Espera 2 segundos para que la página se cargue antes de continuar.

Nota:
- Este uso de time.sleep(2) es simple pero no recomendable para producción.
Lo ideal es usar WebDriverWait para esperar elementos específicos.
"""

from selenium.webdriver.common.by import By
import time


def login(driver):
    # Paso 1: Abrir la página de login
    driver.get("https://www.saucedemo.com/")

    # Paso 2: Llenar los campos de usuario y contraseña
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # Paso 3: Hacer clic en el botón de login
    driver.find_element(By.ID, "login-button").click()

    # Paso 4: Esperar 2 segundos para que la página cargue
    # DATO: Reemplazar este sleep con una espera explícita
    time.sleep(2)
