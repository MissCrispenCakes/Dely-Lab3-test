from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():


    # Render HTML with count variable
    return render_template("index.html")


if __name__ == "__main__":
    app.run()

