from selenium.webdriver.common.by import By
from selenium import webdriver

def test_inventory(login_in_driver):
    try:
        driver = login_in_driver

        # Validar título
        assert driver.title == "Swag Labs"

        # Validar presencia de productos
        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(products) > 0, "No hay productos visibles en la pagina"
    except Exception as e:
        print(f"Error en test_inventory: {e}")
        raise
    finally:
        driver.quit()




#from selenium.webdriver.common.by import By
#from utils.utils import login

#def test_inventario(driver):
#    login(driver, "standard_user", "secret_sauce")
    
    # Validar título
#    assert driver.title == "Swag Labs"

    # Validar presencia de productos
#    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
#    assert len(productos) > 0

    # Listar el nombre y precio del primer producto
#    nombre = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text
#    precio = productos[0].find_element(By.CLASS_NAME, "inventory_item_price").text
#    print(f"Primer producto: {nombre} - Precio: {precio}")
