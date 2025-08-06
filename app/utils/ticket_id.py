# app/utils/ticket_id.py
def generate_ticket_id(index: int) -> str:
    return f"LM2025-{index:04d}"
