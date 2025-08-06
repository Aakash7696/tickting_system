# app/utils/pdf_generator.py
from fpdf import FPDF
import os

class IndividualPDFGenerator:
    def __init__(self, bg_image="assets/ticket_template.png", output_folder="output/pdfs"):
        self.bg_image = bg_image
        self.output_folder = output_folder
        os.makedirs(self.output_folder, exist_ok=True)

    def generate_ticket_pdf(self, ticket_id, qr_path):
        pdf = FPDF(orientation='L', unit='mm', format=(80, 210))
        pdf.add_page()

        # Background image
        pdf.image(self.bg_image, x=0, y=0, w=210, h=80)

        # QR code placement (adjust position and size)
        pdf.image(qr_path, x=170, y=15, w=35, h=35)

        # Ticket ID placement with bold font
        pdf.set_font("Arial", style='B', size=10)   # 👈 Added style='B'
        pdf.set_xy(166, 49)
        pdf.cell(40, 10, f"TICKET ID : {ticket_id}")


        # Save individual PDF
        pdf_path = os.path.join(self.output_folder, f"{ticket_id}.pdf")
        pdf.output(pdf_path)

        return pdf_path
