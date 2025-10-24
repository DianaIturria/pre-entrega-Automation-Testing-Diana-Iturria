from selenium.webdriver.common.by import By
from selenium import webdriver

def test_login_validation(login_in_driver):
    try:
        driver = login_in_driver

        assert "/inventory.html" in driver.current_url, "No se redirgio al inventario"

    except Exception as e:
        print(f"Error en test_login: {e}")
        raise
    finally:
        driver.quit()
    






#from selenium.webdriver.common.by import By
#from utils.utils import login

#def test_login_exitoso(driver):
#    login(driver, "standard_user", "secret_sauce")
#    assert "inventory.html" in driver.current_url
#    titulo = driver.find_element(By.CLASS_NAME, "app_logo").text
#    assert titulo == "Swag Labs"



#from selenium.webdriver.common.by import By

#def test_login_validation(login_in_driver):
#    driver = login_in_driver
#    assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
#    print("✅ Login correcto: redirigió al inventario.")
