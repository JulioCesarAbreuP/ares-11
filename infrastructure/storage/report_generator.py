# infrastructure/storage/report_generator.py
"""
Genera un informe PDF profesional con logos NIST/CIS, tabla de riesgos, rutas de ataque y recomendaciones.
Formalizado para arquitectura enterprise.
"""

from fpdf import FPDF
import datetime
from core.utils import log_event, trace, retry, sanitize_input
from core.contracts import PDFReportRequest, PDFReportResult

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'ARES-11 - Informe Técnico de Auditoría', 0, 1, 'C')
        self.image('docs/ADR/nist-logo.png', 10, 8, 20)
        self.image('docs/ADR/cis-logo.png', 180, 8, 20)
        self.ln(10)
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

@trace(stage="report_generator")
@retry(retries=2, delay=1.0)
def generate_pdf_report(request: PDFReportRequest) -> PDFReportResult:
    findings = [sanitize_input(f) for f in request.findings]
    attack_paths = [sanitize_input(p) for p in request.attack_paths]
    filename = sanitize_input(request.filename or 'ARES11-Informe.pdf')
    try:
        pdf = PDF()
        pdf.add_page()
        pdf.set_font('Arial', '', 11)
        pdf.cell(0, 10, f'Fecha: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}', 0, 1)
        pdf.ln(5)
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(0, 10, 'Resumen de Riesgos', 0, 1)
        pdf.set_font('Arial', '', 10)
        for f in findings:
            pdf.multi_cell(0, 8, f"- {f.get('ioc', f.get('finding', ''))} | Severidad: {f.get('severity', f.get('risk_level', ''))}\nDefensa: {f.get('defense', f.get('ms_defense', ''))}")
        pdf.ln(5)
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(0, 10, 'Rutas de Ataque Detectadas', 0, 1)
        pdf.set_font('Arial', '', 10)
        for p in attack_paths:
            pdf.multi_cell(0, 8, f"{p['path']} | Severidad: {p['severity']}")
        pdf.output(filename)
        log_event("report.generated", {"filename": filename}, context={"stage": "report_generator"})
        return PDFReportResult(filename=filename)
    except Exception as e:
        log_event("report_generator.error", str(e), context={"stage": "report_generator"})
        raise
    print(f"[+] Informe PDF generado: {filename}")
