from flask import Flask, request, render_template_string
import redis
import os
import time

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "redis")

# 🔁 Retry connection to Redis
for i in range(10):
    try:
        r = redis.Redis(host=redis_host, port=6379)
        r.ping()
        print("Connected to Redis!")
        break
    except redis.exceptions.ConnectionError:
        print("Waiting for Redis...")
        time.sleep(2)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Voting App</title>
</head>
<body>
    <h1>Vote for your favorite!</h1>
    <form method="POST">
        <button name="vote" value="Cats">Cats</button>
        <button name="vote" value="Dogs">Dogs</button>
    </form>
    <h2>Results:</h2>
    <p>Cats: {{cats}}</p>
    <p>Dogs: {{dogs}}</p>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def vote():
    if request.method == "POST":
        choice = request.form["vote"]
        r.incr(choice)

    cats = r.get("Cats") or 0
    dogs = r.get("Dogs") or 0

    return render_template_string(
        HTML,
        cats=int(cats),
        dogs=int(dogs)
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)