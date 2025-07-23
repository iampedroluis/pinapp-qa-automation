# POM para la pagina de registro

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistroPage:
    """
    Esta clase encapsulará las rutas y acciones de la página de registro.

    "NOTA": El registro de un usario requiere que complete algunos datos en la pagina de login, hacer click en el botón de registro y luego completar el formulario de registro.
    """
    url = "https://automationexercise.com/login"
    
    def __init__(self, driver):
        """  
        Args:
            driver: El controlador de Selenium para interactuar con la página.
        """
        self.driver = driver
        
        #Locators:
        
        # XPaths de los elementos de la página de login y registro (/login)
        self.title_signup_xpat = '//h2[contains(text(),"New User Signup!")]'
        self.name_input_xpath = '//input[@type="text" and @name="name"]'
        self.email_input_xpath = '//input[@type="email" and @name="email" and @data-qa="signup-email"]'
        self.button_signup_xpath = '//button[@type="submit" and contains(text(), "Signup")]'
        
        
        
        # XPaths de los elementos del formulario de registro (/signup)
        
    
    #Metodos
    
    def wait_for_title_visible(self):
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.text_to_be_present_in_element((By.XPATH, self.title_signup_xpat),"New User Signup!"))
        return element
    
    def complete_input_name(self, name):
        name_input = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.name_input_xpath)))
        name_input.clear()
        name_input.send_keys(name)
    
    def complete_input_email(self, email):
        email_input = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.email_input_xpath)))
        email_input.clear()
        email_input.send_keys(email)