import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.by import By
import time 


#Marca para el test de registro de usuario (PIA_001)
pytestmark = pytest.mark.PIA_001
# Carga de los escenarios del archivo test_registro.feature
scenarios('../features/test_registro.feature')


#Pasos del caso de prueba 
@given('que el usuario accede a la página principal')
def que_el_usuario_accede_a_la_pagina_principal(driver, home_page):
    driver.get(home_page.url)
    assert "Home" in driver.page_source

@when('hace clic en el botón Signup / Login')
def hace_clic_en_el_boton_signup_login(home_page):
    home_page.click_signup_login()
    

@then('debería ser redirigido a la página de login')
def deberia_ser_redirigido_a_la_pagina_de_login(driver, registro_page):
    assert registro_page.wait_for_title_visible(), "El título 'New User Signup!' no está visible"
    assert "/login" in driver.current_url, "No se redireccionó correctamente al login"
    

@when(parsers.cfparse('completa el campo Name con "{nombre}"'))
def completa_el_campo_Name_con_nombre(registro_page, nombre):
    registro_page.type_input_name(nombre)

@when(parsers.cfparse('completa el campo Email Address con "{email}"'))
def completa_el_campo_email_address_con_email(registro_page, email):
    registro_page.type_input_email(email)


@when('hace clic en el botón Signup')
def hace_clic_en_el_boton_signup(registro_page):
    registro_page.click_signup_button()

    
@then('debería visualizar el formulario de creación de cuenta')
def deberia_visualizar_el_formulario_de_creacion_de_cuenta(registro_page):
    assert registro_page.title_signup_form_visible(), "El titulo Enter Account Information no esta en la pagina"
    
@when('selecciona el título Mr.')
def selecciona_el_titulo_mr(registro_page):
    registro_page.click_on_mr_radio_button()

@when(parsers.cfparse('completo el campo password con valor "{password}"'))
def completo_el_campo_password(registro_page, password):
    registro_page.type_input_password(password)

@when(parsers.cfparse('completa la fecha de nacimiento con "{dia}", "{mes}", "{año}"'))
def completa_la_fecha_de_naciemineto(registro_page, dia, mes, año):
    registro_page.select_day(dia)
    registro_page.select_month(mes)
    registro_page.select_year(año)

@when('marca la opción Receive special offers from our partners!')
def marca_la_opcion_recive_special_offers_from_our_partners(registro_page):
    registro_page.click_checkbox_offers()
    
@when(parsers.cfparse('completa el campo First name con "{nombre}"'))
def completa_el_campo_first_name(registro_page, nombre):
    registro_page.type_first_name_input(nombre)
    
@when(parsers.cfparse('completa el campo Last name con "{apellido}"'))
def completa_el_campo_last_name(registro_page, apellido):
    registro_page.type_last_name_input(apellido)
    
@when(parsers.cfparse('completa el campo Company con "{compañia}"'))
def completa_el_campo_company(registro_page, compañia):
    registro_page.type_company_input(compañia)

@when(parsers.cfparse('completa el campo Address con "{direccion}"'))
def completa_el_campo_address(registro_page, direccion):
    registro_page.type_address1_input(direccion)

@when(parsers.cfparse('selecciona el país "{pais}"'))
def selecciona_el_pais(registro_page, pais):
    registro_page.select_country(pais)

@when(parsers.cfparse('completa el campo State con "{estado}"'))
def completa_el_campo_state(registro_page, estado):
    registro_page.type_state_input(estado)

@when(parsers.cfparse('completa el campo City con "{ciudad}"'))
def completa_el_campo_city(registro_page, ciudad):
    registro_page.type_city_input(ciudad)

@when(parsers.cfparse('completa el campo Zipcode con "{codigoPostal}"'))
def completa_el_campo_zipcode(registro_page, codigoPostal):
    registro_page.type_zipcode_input(codigoPostal)

@when(parsers.cfparse('completa el campo Mobile Number con "{telefono}"'))
def completa_el_campo_mobile_number(registro_page, telefono):
    registro_page.type_mobile_number_input(telefono)

@when('hace clic en el botón Create Account')
def hace_clic_en_el_boton_create_account(registro_page):
    registro_page.click_button_create_account()

@then('debería visualizar el mensaje Account Created!')
def deberia_visualizar_el_mensaje_accounted_created(accountCreated_page):
    assert accountCreated_page.created_accounted_title_visible(), "El titulo Account Created! no esta en la pagina"
    