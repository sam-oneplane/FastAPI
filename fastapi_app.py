from fastapi import FastAPI
from pydantic import BaseModel
from loaners_data import LoanersRequirements, Operators
from typing import Dict, Tuple, Callable

app = FastAPI()

class LoanDetails(BaseModel):
    req_amount : int
    borrow_type: str
    loan_type: str
    industry: str
    state: str
    risk_level:int

class Response(BaseModel):
    approved_loaners : list[str]        


class Loaner:
    def __init__(self, name: str, loan_requirements : Dict[str, Tuple[int, Callable]]):
        self.name = name
        self.loan_requirements = loan_requirements
        self.constraints = len(loan_requirements)

    def is_loan_approved(self, loan_request : LoanDetails) -> bool:
        res : bool = True
        loan_request_keys = LoanDetails.model_fields.keys()
        for key, (value, operator) in self.loan_requirements.items():
            try :
                if not key in loan_request_keys:
                    result =  False
                loan_request_value = getattr(loan_request, key)
                
                res = operator(loan_request_value, value)
                    
            except Exception as e:
                print(e)
                result = False

            if res == False:
                    break
            
        return res
    
# laze generation of Loaner objects
def get_loaner_requirements():
    for key, value in LoanersRequirements.items():
        yield Loaner(key, value)


@app.post("/applicationMatch", response_model=Response)
def get_request(request: LoanDetails):

    loan_requirements = get_loaner_requirements()
    approved_loaners : list[Tuple[str, int]] = []
    # iter over generator function
    for gen_loaner in loan_requirements:
        if gen_loaner.is_loan_approved(request):
            approved_loaners.append((gen_loaner.name, gen_loaner.constraints))
    if len(approved_loaners) > 2:
        approved_loaners.sort(key=lambda x: x[1], reverse=True)
        return {"approved_loaners": [x[0] for x in approved_loaners[:2]]}
    return {"approved_loaners": [x[0] for x in approved_loaners]}

