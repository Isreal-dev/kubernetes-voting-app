FROM python:3.9-slim
WORKDIR /app
# Change this line:
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]