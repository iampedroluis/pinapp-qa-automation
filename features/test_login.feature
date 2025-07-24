@PIA_002
Feature: Login de usuario

  #Criterio de Aceptacion
#   Como usuario registrado
#   Quiero poder iniciar sesión desde la pestaña Home
#   Para acceder a mi cuenta desde la sección de Login

  Scenario: Login exitoso desde la pestaña Home
    Given que me encuentro en la pestaña Home
    When hago clic en el botón SignUp/Login
    And soy redirigido a la pestaña de Login
    And completo el campo Email con "test.uat02@example.com"
    And completo el campo Password con "123456"
    And hago clic en el botón Login
    Then se muestra el mensaje Logged in as

