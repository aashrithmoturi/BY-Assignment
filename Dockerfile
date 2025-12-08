FROM python:3.11-slim

# set the working directory
WORKDIR /app

# install system dependencies required for psycopg2
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && apt-get clean

# copy requirement files
COPY requirements.txt .

# install python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy everything
COPY . .

# expose FastAPI port
EXPOSE 8000

# run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
