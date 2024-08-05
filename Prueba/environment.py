import os
from fpdf import FPDF
from datetime import datetime

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Reporte de Pruebas', ln=True, align='C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()} | Generado el {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}', align='C')

    def add_chapter_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, title, ln=True, align='L')
        self.ln(5)

    def add_paragraph(self, text):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, text)
        self.ln()

    def add_screenshot(self, image_path, caption):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, caption, ln=True, align='C')
        self.image(image_path, x=10, w=190)
        self.ln(10)

def before_all(context):
    # Crear directorio para los reportes si no existe
    os.makedirs('reports', exist_ok=True)
    print("Directorio 'reports' creado o ya existente.")

def before_scenario(context, scenario):
    # Inicializar el documento PDF para cada escenario
    context.pdf = PDF()
    context.pdf.set_auto_page_break(auto=True, margin=15)
    context.pdf.add_page()

    # Agregar portada al PDF
    context.pdf.set_font('Arial', 'B', 20)
    context.pdf.cell(0, 60, 'Reporte de Escenario', ln=True, align='C')
    context.pdf.set_font('Arial', 'I', 16)
    context.pdf.cell(0, 10, f'Escenario: {scenario.name}', ln=True, align='C')
    context.pdf.set_font('Arial', '', 12)
    context.pdf.ln(20)
    context.pdf.cell(0, 10, f'Fecha: {datetime.now().strftime("%Y-%m-%d")}', ln=True, align='C')
    context.pdf.ln(30)
    context.pdf.set_font('Arial', '', 12)
    
    context.pdf.add_page()
    context.pdf.add_chapter_title('1. Detalles del Escenario')
    context.pdf.add_paragraph(
        "Este escenario se enfoca en validar las funcionalidades al iniciar sesion "
        "Se presentaran los resultados de las pruebas realizadas."
    )

    print(f"PDF inicializado para el escenario: {scenario.name}")

def after_step(context, step):
    if step.status == 'failed':
        screenshot_path = f'screenshots/{step.name.replace(" ", "_")}.png'
        context.driver.save_screenshot(screenshot_path)

        context.pdf.add_screenshot(screenshot_path, f'Fallo en: {step.name}')
        print(f"Captura de pantalla guardada: {screenshot_path}")

def after_scenario(context, scenario):
    context.pdf.add_page()
    context.pdf.add_chapter_title('Status del Escenario')
    if hasattr(scenario, 'status'):
        if scenario.status == 'passed':
            context.pdf.add_paragraph("El escenario ha pasado todas las pruebas exitosamente.")
        else:
            context.pdf.add_paragraph(
                "El escenario no ha pasado todas las pruebas. Por favor revise los detalles y errores mostrados anteriormente."
            )

    # Guardar el PDF después de cada escenario
    pdf_filename = f'reports/{scenario.name.replace(" ", "_")}.pdf'
    context.pdf.output(pdf_filename)
    print(f"Reporte guardado como {pdf_filename}")

    # Finalizar el navegador después de cada escenario
    if hasattr(context, 'driver'):
        context.driver.close()
        print("Navegador cerrado correctamente.")
