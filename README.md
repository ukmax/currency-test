## How to start

Clone the repository, then install the requirements and start the web server.

    $ pip install -r requirements.txt
    $ uvicorn app:app --reload

## API endpoints

#### GET /rate?currency=var1&date=var2

**Parameters**

|       Name | Required |  Type   | Description                                                                                                 |
|-----------:|:--------:|:-------:|-------------------------------------------------------------------------------------------------------------|
| `currency` | required | string  | Supported values: `USD`, `EUR` or `CNY`.                                                                    |
|     `date` | required | string  | Supported values:<br/>`2022-04-25`,<br/>`2022-04-26`,<br/>`2022-04-27`,<br/>`2022-04-28`,<br/>`2022-04-29`. |

**Response**

```
{
   "currency":"currency",
   "date":"date",
   "rate":"rate"
}
```
### GET /help