import time
import redis
import psycopg2
import os

redis_host = os.getenv("REDIS_HOST", "redis")
db_host = os.getenv("DB_HOST", "db")

# Connect to Redis
for i in range(10):
    try:
        r = redis.Redis(host=redis_host, port=6379)
        r.ping()
        break
    except:
        print("Waiting for Redis...")
        time.sleep(2)

# Connect to Postgres
for i in range(10):
    try:
        conn = psycopg2.connect(
            host=db_host,
            user="postgres",
            password="postgres",
            database="votes"
        )
        cur = conn.cursor()
        break
    except:
        print("Waiting for Postgres...")
        time.sleep(2)

# Create table
cur.execute("CREATE TABLE IF NOT EXISTS votes (vote VARCHAR(255))")
conn.commit()

print("Worker started...")

# Process votes
while True:
    vote = r.lpop("votes")
    if vote:
        cur.execute("INSERT INTO votes (vote) VALUES (%s)", (vote.decode("utf-8"),))
        conn.commit()
        print("Saved vote:", vote)
    else:
        time.sleep(1)