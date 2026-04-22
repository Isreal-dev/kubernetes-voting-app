FROM python:3.9-slim
WORKDIR /app
# Change this line:
COPY . .
RUN pip install --no-cache-dir redis psycopg2-binary
CMD ["python", "app.py"]