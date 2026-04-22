FROM python:3.9-slim
WORKDIR /app

# Change this to point to the worker folder
COPY app/worker/ .

# Since you don't have a requirements.txt here, we keep your manual install
RUN pip install --no-cache-dir redis psycopg2-binary

CMD ["python", "app.py"]