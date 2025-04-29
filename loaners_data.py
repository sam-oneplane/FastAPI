
Operators = {
    "eq" : lambda x, y: str(x).strip(' ').lower() == str(y).strip(' ').lower(),
    "lte" : lambda x, y: x>0 and x<=y,
    "gte" : lambda x, y: x>=y,
    "in" : lambda x,y: isinstance(y, list) and  x in set(y)  
}

LoanersRequirements  = {  "FirstStamBank":  {"risk_level": (80, Operators["lte"])},
                          "GeneralCitizenBank":  {"risk_level": (60, Operators["lte"]), 
                                            "loan_type" : ("Student Loan", Operators["eq"]), 
                                            "state": (["CA", "NY"], Operators["in"])},
                          "SaltNPaperBank":   {"risk_level": (80, Operators["lte"]), 
                                            "borrow_type" : ("business", Operators["eq"]),
                                            "req_amount": (500000, Operators["gte"])},
                          "FirstVirtualBank": {"loan_type": ("Line of Credit", Operators["eq"]), 
                                            "industry": ("Resturant", Operators["eq"])},
                          "InternetionalBank": {"req_amount": (200000, Operators["lte"])},
                          "PrivateDirtyBank" : {"loan_type": (["Line of Credit", "Student Loan"], Operators["in"]),
                                               "risk_level": (50, Operators["lte"]),
                                               "borrow_type" : (["business", "consumer"], Operators["in"]),
                                               "state": (["CA", "NY"], Operators["in"])
                                              }
}

