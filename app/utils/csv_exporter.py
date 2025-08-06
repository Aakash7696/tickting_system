# app/utils/csv_exporter.py
import csv
import os
from app.db import tickets_collection

def export_tickets_to_csv(filename="output/tickets.csv"):
    # Output folder bana le agar nahi hai to
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # File khol aur likhna start kar
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Header row likh
        writer.writerow(["ticket_id", "encrypted_data", "status"])

        # MongoDB se sab ticket nikaal
        for ticket in tickets_collection.find():
            writer.writerow([
                ticket.get("ticket_id", ""),
                ticket.get("encrypted_data", ""),
                ticket.get("status", "unused")
            ])
    
    return filename
