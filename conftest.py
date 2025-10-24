import pytest
from selenium import webdriver
from utils import login

@pytest.fixture
def driver():
    # Inicializa el navegador
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Decorador para iniciar sesión en el navegador
@pytest.fixture
def login_in_driver(driver):
    login(driver)
    return driver



