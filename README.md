To run the service locally without docker:

1. Create a virtual environment for packages to not override other package versions using command: python -m venv <my-env>

2. In the <my-env> folder, copy the path for powershell(.ps1 extension) and paste it in the powershell

3. pip install -r .\requirements.txt

4. In the .env file update the username, password and DB name

5. make sure to give the local db url: run the service using the command : uvicorn app.main:app



To run the service using docker container(make sure to give the url by referring the container name of the db in docker-compose file): run docker-compose up --build



FAQs:
- to come out of the created virtual environment need to hit the command : deactivate