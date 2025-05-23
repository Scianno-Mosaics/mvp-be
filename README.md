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
poetry run uvicorn mvp_be.main:app --reload --port 8080
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

## Dcoker build to test locally
docker build -t mvp:latest .
docker run -p 8081:8080 mvp-be:latest

docker build --no-chache -t mvp-be .
docker run -p 8081:8080 mvp-be


## Google cloud run build and deploy

- set up Global load balancer

 - DNS

 - deploy containe



gcloud auth login
gcloud config set project mvp-app-459119


gcloud builds submit --tag us-central1-docker.pkg.dev/mvp-app-459119/my-repo/mvp-be .



gcloud run deploy mvp-be --image us-central1-docker.pkg.dev/mvp-app-459119/my-repo/mvp-be --platform managed --region us-central1 --allow-unauthenticated







