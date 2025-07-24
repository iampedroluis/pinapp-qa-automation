from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class AccountCreated:
    
    def __init__(self, driver):
        
        self.driver = driver
        
        
        #Locators 
        self.title_account_created_xpath = '//b[contains(text(),"Account Created!")]'
        
    def created_accounted_title_visible(self):
        try:
            title_accounted_created = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH, self.title_account_created_xpath)))
            return title_accounted_created.is_displayed()
        except:
            return False