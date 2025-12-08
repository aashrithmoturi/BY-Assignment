1. Create a virtual environment for packages to not override other package versions using command: python -m venv <my-env>

2. In the <my-env> folder, copy the path for powershell(.ps1 extension) and paste it in the powershell

3. pip install fastapi uvicorn psycopg2-binary pydantic-settings sqlalchemy

4. In the .env file update the username, password and DB name

5. run the service using the command : uvicorn app.main:app


FAQs:
- to come out of the created virtual environment need to hit the command : deactivate