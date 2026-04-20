from flask import Flask, request, render_template_string

app = Flask(__name__)

votes = {"Cats": 0, "Dogs": 0}

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
        votes[choice] += 1
    return render_template_string(HTML, cats=votes["Cats"], dogs=votes["Dogs"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)