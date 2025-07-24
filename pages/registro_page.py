# POM para la pagina de registro

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class RegistroPage:
    """
    Esta clase encapsulará las rutas y acciones de la página de registro.

    "NOTA": El registro de un usario requiere que se completen algunos datos en la pagina de /login, hacer click en el botón de registro y luego completar el formulario de registro.
    """
    url = "https://automationexercise.com/login"
    
    def __init__(self, driver):
        """  
        se inician las rutas con xpaths
        param:
            driver: El controlador de Selenium para interactuar con la página.
        """
        self.driver = driver
        
        #Locators:
        
        # XPaths de los elementos de la página de registro ()
        self.title_signup_xpath = '//h2[contains(text(),"New User Signup!")]'
        self.name_input_xpath = '//input[@type="text" and @name="name"]'
        self.email_input_xpath = '//input[@type="email" and @name="email" and @data-qa="signup-email"]'
        self.button_signup_xpath = '//button[@type="submit" and contains(text(), "Signup")]'
        
        
        
        # XPaths de los elementos del formulario de registro (/signup)
        self.title_signup_form_xpath = '//b[contains(text(),"Enter Account Information")]'
        self.mr_radio_button_xpath = '//input[@type="radio" and @value="Mr"]'
        self.type_input_password_xpath = '//input[@type="password" and @id="password"]'
        self.day_select_xpath = '//select[@name="days"]'
        self.month_select_xpath = '//select[@name="months"]'
        self.year_select_xpath = '//select[@name="years"]'
        self.checkbox_offers_xpath = '//input[@type="checkbox" and @name="optin"]'
        self.first_name_input_xpath = '//input[@type="text" and @id="first_name"]'
        self.last_name_input_xpath = '//input[@type="text" and @id="last_name"]'
        self.company_input_xpath = '//input[@type="text" and @id="company"]'
        self.address1_input_xpath = '//input[@type="text" and @name="address1"]'
        self.country_select_xpath = '//select[@name="country"]'
        self.state_input_xpath = '//input[@name="state"]'
        self.city_input_xpath = '//input[@name="city"]'
        self.zipcode_input_xpath = '//input[@name="zipcode"]'
        self.mobile_number_input_xpath = '//input[@name="mobile_number"]'
        self.create_account_button_xpath = '//button[@type="submit" and contains(text(),"Create Account")]'

        
    #Metodos
    def wait_for_title_visible(self):
        """
        metodo para esperar que el titulo este visible
        """
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.text_to_be_present_in_element((By.XPATH, self.title_signup_xpath),"New User Signup!"))
        return element
    
    def type_input_name(self, name):
        """
        Metodo para completar el input de name del registro 
        param: 
            name: el argumento se envia desde el caso de prueba del gherkins
        """
        name_input = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.name_input_xpath)))
        name_input.clear()
        name_input.send_keys(name)
    
    def type_input_email(self, email):
        """
        Metodo para completar el input del email del registro
        param: 
            email: el parametro se envia desde el caso de prueba del gherkins
        """
        email_input = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.email_input_xpath)))
        email_input.clear()
        email_input.send_keys(email)
        
    def click_signup_button(self):
        """
        Metodo para hacer clic en el boton Signup
        """
        signup_button = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH, self.button_signup_xpath)))
        signup_button.click()
        
    def title_signup_form_visible(self):
        try:
            title_form = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH, self.title_signup_form_xpath)))
            return title_form.is_displayed()
        except:
            return False
    
    def click_on_mr_radio_button(self):
        radio_button = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH, self.mr_radio_button_xpath)))
        radio_button.click()
    
    def type_input_password(self, password):
        """
        funcion para escribir la password
        param: password: se envia desde el caso de prueba
        """
        input_password = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.type_input_password_xpath)))
        input_password.clear()
        input_password.send_keys(password)
    
    def select_day(self, day):
        """
        funcion para seleccionar el dia 
        param: day: se envia el dia en el caso de prueba
        """
        selection_day = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH, self.day_select_xpath)))
        select = Select(selection_day)
        select.select_by_value(day)
        
    def select_month(self, month):
        """
        funcion para seleccionar el mes
        param: month: se envia el paramentro en el caso de prueba
        """
        selection_month = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH, self.month_select_xpath)))
        select = Select(selection_month)
        select.select_by_visible_text(month)
        
    def select_year(self, year):
        """
        Funcion para seleccionar el año
        param: year: se envia el paramwtro desde el caso de prueba
        """
        selection_year = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.year_select_xpath)))
        select = Select(selection_year)
        select.select_by_value(year)
        
    def click_checkbox_offers(self):
        """
        en esta funcion se agrega un time.sleep() de 1s ya que la pagina suele contener iframe de google Ads y no realiza la ejecucion deseada.
        """
        checkbox = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_offers_xpath)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
        time.sleep(1) 
        checkbox.click()
        
    def type_first_name_input(self, first_name):
        type_firstName = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.first_name_input_xpath)))
        type_firstName.clear()
        type_firstName.send_keys(first_name)
        
    def type_last_name_input(self, last_name):
        type_lastName = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.last_name_input_xpath)))
        type_lastName.clear()
        type_lastName.send_keys(last_name)
        
    def type_company_input(self, company):
        """
        Metodo para escribir el nombre de la compañia
        param: company: este parametro va a venir del caso de prueba 
        """
        type_company = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.company_input_xpath)))
        type_company.clear()
        type_company.send_keys(company)
        
    def type_address1_input(self, address):
        type_address1 = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.address1_input_xpath)))
        type_address1.clear()
        type_address1.send_keys(address)
        
    def select_country(self, country):
        selection_country = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.country_select_xpath)))
        select = Select(selection_country)
        select.select_by_value(country)        
        
    def type_state_input(self, state):
        type_state = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.state_input_xpath)))
        type_state.clear()
        type_state.send_keys(state)
        
    def type_city_input(self, city):
        type_city = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.city_input_xpath)))
        type_city.clear()
        type_city.send_keys(city)
        
    def type_zipcode_input(self, zipcode):
        type_zipcode = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.zipcode_input_xpath)))
        type_zipcode.clear()
        type_zipcode.send_keys(zipcode)
        
    def type_mobile_number_input(self, mobile_number):
        type_mobile_number = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.mobile_number_input_xpath)))
        type_mobile_number.clear()
        type_mobile_number.send_keys(mobile_number)
        
    def click_button_create_account(self):
        create_account_button = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH, self.create_account_button_xpath)))
        create_account_button.click()
        
