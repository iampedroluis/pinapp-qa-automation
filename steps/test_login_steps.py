import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.by import By
import time 


#Marca para el test de login de usuario (PIA_002)
pytestmark = pytest.mark.PIA_002
# Carga de los escenarios del archivo test_login.feature
scenarios('../features/test_login.feature')


#Pasos del caso de prueba 
@given('que me encuentro en la pestaña Home')
def que_me_encuentro_en_la_pestaña_home(driver, home_page):
    driver.get(home_page.url)
    assert "Home" in driver.page_source

@when('hago clic en el botón SignUp/Login')
def hace_clic_en_el_boton_signup_login(home_page):
    home_page.click_signup_login()
    
@when('soy redirigido a la pestaña de Login')
def soy_redirigido_a_la_pestaña_de_login(login_page):
    print("Assert")
    assert login_page.title_login_visible, "el texto Login to your account no esta en la pestaña"

@when(parsers.cfparse('completo el campo Email con "{email}"'))
def completo_el_campo_email(login_page, email):
    login_page.type_input_email(email)

@when(parsers.cfparse('completo el campo Password con "{password}"'))
def completo_el_campo_password(login_page, password):
    login_page.type_input_password(password)


@when('hago clic en el botón Login')
def hago_clic_en_el_boton_login(login_page):
    login_page.click_login_button()
    
@then('se muestra el mensaje Logged in as')
def se_muestra_el_mensaje(login_page):
    assert login_page.title_logged_visible, "No se encuentra el mensaje Logged in as en la pagina"
