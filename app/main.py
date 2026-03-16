from fastapi import FastAPI
from app.database import Base, engine
from app.routes import address_routes
app = FastAPI(title="Address Book API")

@app.get("/")
def health_check():
    return {"message": "Address Book API is running"}

Base.metadata.create_all(bind=engine)

app.include_router(address_routes.router)
