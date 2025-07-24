# POM para la pagina de home
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    """
    Esta clase encapsulará las rutas y acciones de la página de inicio (home).
    """
    url = "https://automationexercise.com/"


    def __init__(self, driver):
        """
        Inicializa la página de inicio con el controlador de Selenium.
        param:
            driver: El controlador de Selenium para interactuar con la página.
        """
        self.driver = driver
        
        # tiempo de espera para que los elementos sean visibles
        
        
        # Locators:
        # XPaths de los elementos de la página de inicio
        self.signup_login_button_xpath = '//a[@href="/login"]'
        

    def click_signup_login(self):
        """
        clic en el botón de "Signup / Login".
        espera 5 segundos para que el botón sea clickeable.
        """
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.signup_login_button_xpath)))
        element.click()