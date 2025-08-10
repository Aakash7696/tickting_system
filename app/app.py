# Import required modules
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importing the router for the modules
# User Module
from app.routes.scan import router as scan_router


# Initialize the FastAPI application
app = FastAPI()

# CORS configuration
# Specifying allowed origins for cross-origin requests, including common local development URLs.
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8001",
    "http://127.0.0.1:5500"
]

# Adding CORS middleware
# Allowing all origins, credentials, methods, and headers for handling cross-origin requests.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Including routers for the application modules
app.include_router(scan_router)

# Health Check Endpoint
@app.get("/health", tags=["Welcome & Health"])
def health_check():
    try:
        # Add a lightweight check for the database or other services
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}

# Welcome Endpoint
@app.get("/", tags=["Welcome & Health"])
def greating(): 
    return "Welcome in Ticket Scanning System."

