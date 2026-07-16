from pydantic import BaseModel

class DecisionRequest(BaseModel):
    merchant_id:str
    transaction_id:str
    action:str
    amount:float
    