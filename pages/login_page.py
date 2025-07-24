# POM para la pagina de login

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    """
    Esta clase encapsulará las rutas y acciones de la página de login.

    
    """
    url = "https://automationexercise.com/"
    
    def __init__(self, driver):
        """  
        se inician las rutas con xpaths
        param:
            driver: El controlador de Selenium para interactuar con la página.
        """
        self.driver = driver
        
        #Locators:
        
        # XPaths de los elementos de la página de login  (/login)
        self.title_login_xpath = '//h2[contains(text(),"Login to your account")]'
        self.email_input_xpath = '//input[@type="email" and @name="email" and @data-qa="login-email"]'
        self.password_input_xpath = '//input[@type="password" and @name="password"]'
        self.button_login_xpath = '//button[@type="submit" and contains(text(), "Login")]'
        self.title_logged_xpath = '//a[contains(text(), "Logged in as")]'
        

        #Metodos
        
    def title_login_visible(self):
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.text_to_be_present_in_element((By.XPATH, self.title_login_visible), "Login to your account"))
        return element
    
    def type_input_email(self, email):
        """
        Metodo para completar el input del email 
        param: email: viene en el caso de prueba
        """
        email_input = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.email_input_xpath)))
        email_input.clear()
        email_input.send_keys(email)
        
    def type_input_password(self, password):
        """
        Metodo para escribir la password en el input
        param: password: viene en el caso de prueba enviado como parametro
        """
        password_input = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH, self.password_input_xpath)))
        password_input.clear()
        password_input.send_keys(password)
        
    def click_login_button(self):
        """
        Metodo para hacer clic en el boton de login e iniciar sesion
        """
        login_button = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH, self.button_login_xpath)))
        login_button.click()
        
    def title_logged_visible(self):
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.text_to_be_present_in_element((By.XPATH, self.title_logged_xpath), "Logged in as"))
        return element