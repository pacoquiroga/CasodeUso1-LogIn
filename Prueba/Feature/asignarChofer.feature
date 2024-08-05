Feature: Asignar Vehículo Viaje Chofer

  Scenario: Ingresar correo en formato no valido
    Given Se inicia el navegador
    When Entra a la opción de Iniciar Sesion
    And Ingresa el correo "fsquiroga2espe.edu.ec"
    And Ingresa contrasena "123456789"
    Then Click en el Botón Iniciar Sesion
    And Observar el mensaje de confirmacion

  Scenario: Ingresar contrasena en formato no valido
    Given Se inicia el navegador
    When Entra a la opción de Iniciar Sesion
    And Ingresa el correo "fsquiroga2@espe.edu.ec"
    And Ingresa contrasena "123456"
    Then Click en el Botón Iniciar Sesion
    And Observar el mensaje de confirmacion

  Scenario: Ingresar correo no valido
    Given Se inicia el navegador
    When Entra a la opción de Iniciar Sesion
    And Ingresa el correo "pedrosanchez@espe.edu.ec"
    And Ingresa contrasena "123456789"
    Then Click en el Botón Iniciar Sesion
    And Observar el mensaje de confirmacion

  Scenario: Ingresar contrasena no valido
    Given Se inicia el navegador
    When Entra a la opción de Iniciar Sesion
    And Ingresa el correo "fsquiroga2@espe.edu.ec"
    And Ingresa contrasena "1234567890"
    Then Click en el Botón Iniciar Sesion
    And Observar el mensaje de confirmacion

  Scenario: Ingresar credenciales correctas
    Given Se inicia el navegador
    When Entra a la opción de Iniciar Sesion
    And Ingresa el correo "fsquiroga2@espe.edu.ec"
    And Ingresa contrasena "123456789"
    Then Click en el Botón Iniciar Sesion
    And Observar el mensaje de confirmacion
