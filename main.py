from fastapi import FastAPI, HTTPException

app = FastAPI()

CUR = {
    "USD": {
        "2022-04-25": 73.5050,
        "2022-04-26": 73.3611,
        "2022-04-27": 72.7089,
        "2022-04-28": 72.8764,
        "2022-04-29": 72.2953,
    },
    "EUR": {
        "2022-04-25": 80.0249,
        "2022-04-26": 77.4651,
        "2022-04-27": 76.6670,
        "2022-04-28": 75.9224,
        "2022-04-29": 75.3117,
    },
    "CNY": {
        "2022-04-25": 11.3057,
        "2022-04-26": 11.2289,
        "2022-04-27": 11.1576,
        "2022-04-28": 11.1223,
        "2022-04-29": 10.9613,
    }
}


@app.get("/rate")
def get_rate(currency: str, date: str):
    try:
        rate = (CUR[currency][date])
    except KeyError as e:
        print("PRINT e= ", e)
        raise HTTPException(status_code=404, detail=f"{e} not found")
    result = {
        "currency": currency,
        "date": date,
        "rate": rate
    }
    return result


@app.get("/help")
def get_help():
    msg = {
        "message": "Return currency rate on date",
        "request pattern": "GET /rate?currency=var1&date=var2",
        "currency list": "USD, EUR, CNY",
        "valid dates": "From 2022-04-25 to 2022-04-29",
        "date format": "YYYY-MM-DD"
    }
    return msg
