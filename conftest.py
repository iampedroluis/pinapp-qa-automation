import pytest
from pages.home_page import HomePage
from pages.registro_page import RegistroPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    """
    Configura el driver de Selenium para las pruebas.
    Este fixture inicializa el navegador Chrome y lo cierra al finalizar la prueba.
    
    Returns:
        WebDriver: El controlador de Selenium configurado para las pruebas.
        
    """
    #ChromeDriverManager se utiliza para gestionar la instalación del controlador de Chrome.
    # Esto asegura que siempre se utilice la versión correcta del controlador.
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
    

@pytest.fixture
def home_page(driver):
    return HomePage(driver)

@pytest.fixture
def registro_page(driver):
    return RegistroPage(driver)