import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import uvicorn

app = FastAPI()

# Definition of the data model for the loan request
class LoanRequest(BaseModel):
    personal_code: str
    amount: int = Field(ge=2000, le=10000)  # Loan amount must be between 2000 and 10000
    period: int = Field(ge=12, le=60)  # Loan period must be between 12 and 60 months

# I decided to put valid personal codes in a separate JSON file for better organization and maintainability
with open("personal_codes.json", "r") as file:
    valid_personal_codes = json.load(file)


# Endpoint to check the loan request
@app.post("/check")
def check_loan(request: LoanRequest):
    # Check modifier based on personal code
    modifier = valid_personal_codes.get(request.personal_code, None)
    if modifier is None:
        raise HTTPException(status_code=400, detail="Invalid personal code")
    
    #=========================================================================================================
    # Here I will implement the logic to calculate the loan approval based on the amount, period, and modifier
    #=========================================================================================================

    return {"message": "Loan request is valid", "modifier": modifier}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)