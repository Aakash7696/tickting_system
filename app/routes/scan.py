from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from app.db import tickets_collection

router = APIRouter()

class QRScanRequest(BaseModel):
    encrypted_data: str

@router.post("/scan/")
def scan_ticket(data: QRScanRequest):
    ticket = tickets_collection.find_one({"encrypted_data": data.encrypted_data})

    if not ticket:
        raise HTTPException(status_code=404, detail="Invalid QR code")

    if ticket["status"] == "used":
        raise HTTPException(status_code=400, detail="Ticket already used")

    # Mark as used
    tickets_collection.update_one(
        {"_id": ticket["_id"]},
        {"$set": {"status": "used", "scanned_at": datetime.utcnow()}}
    )

    return {
        "message": "Ticket successfully marked as used",
        "ticket_id": ticket["ticket_id"]
    }





