import os
from fastapi import APIRouter
from app.db import tickets_collection
from app.utils.qr_generator import encode_ticket_data, generate_qr_code
from app.utils.ticket_id import generate_ticket_id
from app.utils.csv_exporter import export_tickets_to_csv
from app.utils.pdf_generator import IndividualPDFGenerator

router = APIRouter()

@router.post("/generate-tickets")
def generate_tickets():
    output_dir = "output/qr"
    os.makedirs(output_dir, exist_ok=True)
    ticket_count = 3000

    for i in range(1, ticket_count + 1):
        ticket_id = generate_ticket_id(i)
        encrypted = encode_ticket_data(ticket_id)

        qr_path = f"{output_dir}/{ticket_id}.png"
        generate_qr_code(encrypted, qr_path)

        ticket_data = {
            "ticket_id": ticket_id,
            "encrypted_data": encrypted,
            "status": "unused"
        }
        tickets_collection.insert_one(ticket_data)

    return {"message": f"{ticket_count} tickets generated successfully."}


@router.get("/export-csv")
def export_csv():
    file_path = export_tickets_to_csv()
    return {"message": "CSV exported successfully", "file": file_path}


@router.get("/generate-individual-pdfs")
def generate_individual_pdfs():
    pdf_gen = IndividualPDFGenerator()
    count = 0

    for ticket in tickets_collection.find().limit(3000):
        ticket_id = ticket["ticket_id"]
        qr_path = f"output/qr/{ticket_id}.png"
        pdf_gen.generate_ticket_pdf(ticket_id, qr_path)
        count += 1

    return {"message": f"{count} individual ticket PDFs generated."}








