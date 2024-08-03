## Running
```shell
uvicorn main:app --reload
```


## Example curl commands


```shell
curl -X GET "http://127.0.0.1:8000/quotes/"
```

```shell
curl -X GET "http://127.0.0.1:8000/quotes/random/"
```

```shell
curl -X POST "http://127.0.0.1:8000/quotes/" -H "Content-Type: application/json" -d '{"text": "This is a new quote."}'
```

