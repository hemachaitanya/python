from pydantic import BaseModel
from fastapi import fastAPI
from getfunction.investment import investment, investmentReturn

class Investment(BaseModel):