FROM python:3.9-slim
WORKDIR /app

# Change these to point to the result folder
COPY app/result/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/result/ .

CMD ["python", "app.py"]