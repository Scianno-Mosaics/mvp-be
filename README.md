## notes for the splitting into back end

- use poetry
'''
poetry init
poetry add fastapi uvicorn httpx
poetry export -f requirements.txt --output requirements.txt --without-hashes
'''

- to runt tests
```
poetry run pytest
```
- to run the backend using poetry
'''
poetry run uvicorn main:app --reload --port 8081
'''

- curl command

```
curl -X 'POST' \
  'http://127.0.0.1:8081/api/echo' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "message": "who is in space"
}'
```