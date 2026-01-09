from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def person():
    return render_template("main.html")

@app.route("/info/")
def info():
    return render_template("index.html")


# @app.route("/contact/")
# def contact():
#     return render_template("contact.html")

if __name__ == "__main__":
    app.run()