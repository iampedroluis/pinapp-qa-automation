Feature: Gestión de Usuarios vía API

  Scenario: Crear un nuevo usuario
    Given que tengo los datos válidos de un nuevo usuario
    When creo el usuario mediante la API
    Then la respuesta debe tener código 200
    And el id del usuario en la respuesta debe coincidir con el enviado


  Scenario: Obtener un usuario existente
    Given que existe un usuario con username "Neva_Greenholt"
    When consulto el usuario por su username
    Then la respuesta debe contener código 200
    And el campo "username" debe ser "Neva_Greenholt"
    And el campo "firstName" debe ser "Bret"


  Scenario: Editar un usuario existente
    Given que tengo datos actualizados para el usuario "Neva_Greenholt"
    When envío una petición PUT para actualizar el usuario
    Then la respuesta debe contener código 200
    And el mensaje debe indicar que el ID del usuario fue modificado correctamente


  Scenario: Eliminar un usuario existente
    Given que existe un usuario con username "Neva_Greenholt"
    When elimino el usuario mediante la API
    Then la respuesta debe tener código 200
    And debe indicar que el usuario fue eliminado correctamente