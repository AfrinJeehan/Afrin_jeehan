from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    developer_info = {
        "name": "Afrin Jeehan",
        "role": "AI/ML & Robotics Enthusiast",
    }
    return render_template("index.html", info=developer_info)

if __name__ == "__main__":
    app.run(debug=True)
