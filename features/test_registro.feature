@PIA_001
Feature: Registro de nuevo usuario en Automation Exercise
  #CRITERIO DE ACEPTACIÓN
  
  # Como usuario nuevo
  # Quiero poder registrarme desde la página principal
  # Para acceder a todas las funcionalidades de la plataforma


  Scenario: Registro exitoso desde la página de inicio
    Given que el usuario accede a la página principal 
    When hace clic en el botón Signup / Login
    Then debería ser redirigido a la página de login 

    When completa el campo Name con "Juan Pérez"
    And completa el campo Email Address con "juan.perez@example.com"
    # And hace clic en el botón "Signup"
    # Then debería visualizar el formulario de creación de cuenta

    # When selecciona el título "Mr."
    # And completa la fecha de nacimiento con "10", "May", "1990"
    # And marca la opción "Receive special offers from our partners!"

    # And completa el campo "First name" con "Juan"
    # And completa el campo "Last name" con "Pérez"
    # And completa el campo "Company" con "OpenAI"
    # And completa el campo "Address" con "Calle Falsa 123"
    # And completa el campo "Address 2" con "Depto. 4B"
    # And selecciona el país "Canada"
    # And completa el campo "State" con "Ontario"
    # And completa el campo "City" con "Toronto"
    # And completa el campo "Zipcode" con "A1B2C3"
    # And completa el campo "Mobile Number" con "+1 234 567 8900"

    # And hace clic en el botón "Create Account"
    # Then debería visualizar el mensaje "Account Created!"
