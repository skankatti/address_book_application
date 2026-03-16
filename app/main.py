from fastapi import FastAPI

app = FastAPI(title="Address Book API")

@app.get("/")
def health_check():
    return {"message": "Address Book API is running"}