from flask import Flask
import psycopg2
import time
import os

app = Flask(__name__)

db_host = os.getenv("DB_HOST", "db")

# Connect to DB
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
        print("Waiting for DB...")
        time.sleep(2)

@app.route("/")
def result():
    cur.execute("SELECT vote, COUNT(*) FROM votes GROUP BY vote")
    results = cur.fetchall()

    output = "<h1>Results</h1>"
    for row in results:
        output += f"<p>{row[0]}: {row[1]}</p>"

    return output

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)