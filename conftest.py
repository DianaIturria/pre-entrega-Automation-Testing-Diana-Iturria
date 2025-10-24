import pytest
from selenium import webdriver
from utils import login

@pytest.fixture
def driver():
    # Inicializa el navegador Chrome antes de cada test y lo cierra al finalizar
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Iniciar sesión en el navegador
# Permite reutilizar el login en varios tests sin repetir código.
@pytest.fixture
def login_in_driver(driver):
    login(driver)
    return driver
