from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import os

# Configuración del navegador
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--disable-extensions')
options.add_argument('--no-sandbox')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-browser-side-navigation')
options.add_argument('--disable-gpu')

def take_screenshot(context, step_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_dir = "screenshots"
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    screenshot_name = os.path.join(screenshot_dir, f"{step_name}_{timestamp}.png")
    context.driver.save_screenshot(screenshot_name)
    context.pdf.add_screenshot(screenshot_name, step_name)
    print(f"Screenshot taken: {screenshot_name}")
    return screenshot_name

def mark_step_as_failed(context, step_name, exception):
    print(f"Error in '{step_name}': {exception}")
    raise Exception(f"Step failed: {step_name}. Error: {exception}")

def mark_step_as_passed(context, step_name):
    print(f"Step passed: {step_name}")

@given('Se inicia el navegador')
def iniciarNavegador(context):
    context.driver = webdriver.Chrome(options=options)
    context.failed_steps = []
    print("Browser started")

@when('Entra a la opción de Iniciar Sesion')
def asignar(context):
    try:
        context.driver.maximize_window()
        context.driver.get("file:///C:/xampp/htdocs/CU1/CU1.html")
        take_screenshot(context, '1. Entra a la opción de Iniciar Sesion')
        print("Entered 'Iniciar Sesion' option")
    except Exception as e:
        mark_step_as_failed(context, 'entra_opcion_iniciar_sesion', e)

@when('Ingresa el correo "{correo}"')
def escogerChofer(context, correo):
    try:
        select_element = context.driver.find_element(By.XPATH, '//*[@id="email"]')
        select_element.send_keys(correo)  # Seleccionar por texto visible
        take_screenshot(context, '2. Ingresar_correo')
        print(f"Correo: {correo}")
    except Exception as e:
        mark_step_as_failed(context, 'ingresar_correo', e)

@when('Ingresa contrasena "{contrasena}"')
def escogerVehiculo(context, contrasena):
    try:
        select_element = context.driver.find_element(By.XPATH, '//*[@id="password"]')
        select_element.send_keys(contrasena) # Seleccionar por texto visible
        take_screenshot(context, '3. Ingresar_contrasena')
        print(f"Contrasena: {contrasena}")
    except Exception as e:
        mark_step_as_failed(context, 'ingresar_contrasena', e)


@then('Click en el Botón Iniciar Sesion')
def clickAsignar(context):
    try:
        button = context.driver.find_element(By.XPATH, '//*[@id="registerForm"]/div[3]/input')
        button.click()
        take_screenshot(context, '6. Click en el Botón Iniciar Sesion')
        print("Clicked 'Iniciar Sesion' button")
    except Exception as e:
        mark_step_as_failed(context, 'click_iniciar_sesion', e)
        print(f"Exception occurred: {e}")
        raise e


@then('Observar el mensaje de confirmacion')
def verificarMensaje(context):
    try:
        # Esperar a que el modal de confirmación aparezca
        WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="successMessage"]'))
        )
        confirmation_message = context.driver.find_element(By.XPATH, '//*[@id="successMessage"]')
        # Si el elemento se encuentra, el paso es exitoso
        take_screenshot(context, '7. Observar el mensaje de confirmacion')
        mark_step_as_passed(context, 'verificar_mensaje')
    except Exception as e:
        # Si ocurre una excepción, el paso falla
        mark_step_as_failed(context, 'verificar_mensaje', e)