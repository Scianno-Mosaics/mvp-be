## notes for the splitting into back end

- use poetry
'''
poetry init
poetry add fastapi uvicorn httpx
poetry export -f requirements.txt --output requirements.txt --without-hashes
'''

- to run the backend using poetry
'''
poetry run uvicorn app.main:app --reload --port 8000
'''