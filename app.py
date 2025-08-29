from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    timeline = [
        {"year": "1700", "story": "Farms, guilds, handcraft. 🌾"},
        {"year": "1800", "story": "Factories, steam power. 🏭"},
        {"year": "1900", "story": "Mass production, global trade. 🔧"},
        {"year": "2000", "story": "PCs, web, globalization. 💻"},
        {"year": "2025", "story": "AI copilots, automation. 🤖"},
        {"year": "2200", "story": "Human–AI symbiosis, space infra? 🚀"}
    ]
    return render_template("index.html", timeline=timeline)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
