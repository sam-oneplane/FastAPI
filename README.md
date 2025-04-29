# FastAPI
A short FastApi App

## Using VSCODE
### Lunch uvicorn server
`uvicorn fastapi_app:app --relaod`

<p> uvicorn is running on <a href=http://127.0.0.1:8000> </a> inline link</p> 


### send curl command on cli
`curl -X POST -H "Content-Type: application /json" -d '{"key"|"value"}' 'http://127.0.0.1/applicationMatch'`

### Use interactive api
<p> in browser:   http://127.0.0.1:8000/docs# inline link</p> 
or
<p> in browser:   http://127.0.0.1:8000/redoc inline link</p> 

##### Request data example:
```
{
    "req_amount" : 30000,
    "borrow_type": "Customer"
    "loan_type": "Student Loan"
    "industry": ""
    "state": "NY"
    "risk_level": 65
}
```
