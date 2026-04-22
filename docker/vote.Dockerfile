FROM python:3.9-slim

WORKDIR /app

# 1. Copy only the requirements first (Better for build caching)
COPY app/vote/requirements.txt .

# 2. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copy the actual application code from the subfolder to /app
COPY app/vote/ .

EXPOSE 80

CMD ["python", "app.py"]