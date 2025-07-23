import pytest
from pytest_bdd import scenarios, given, when, then, parsers
import time 


#Marca para el test de registro de usuario (PIA_001)
pytestmark = pytest.mark.PIA_001
# Carga de los escenarios del archivo test_registro.feature
scenarios('../features/test_registro.feature')



@given('que el usuario accede a la página principal')
def que_el_usuario_accede_a_la_pagina_principal(driver, home_page):
    driver.get(home_page.url)
    assert "Home" in driver.page_source

@when('hace clic en el botón Signup / Login')
def hace_clic_en_el_boton_signup_login(home_page):
    home_page.click_signup_login()
    

@then('debería ser redirigido a la página de login')
def deberia_ser_redirigido_a_la_pagina_de_login(registro_page):
    registro_page.wait_for_title_visible()
    

@when(parsers.cfparse('completa el campo Name con "{nombre}"'))
def completa_el_campo_Name_con_nombre(registro_page, nombre):
    registro_page.complete_input_name(nombre)


@when(parsers.cfparse('completa el campo Email Address con "{email}"'))
def completa_el_campo_email_address_con_email(registro_page, email):
    registro_page.complete_input_email(email)
    time.sleep(5)