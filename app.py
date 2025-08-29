from flask import Flask, render_template, request

app = Flask(__name__)

# A small database of stories
stories = {
    "1700": {
        "farmer": "In 1700, as a farmer, your world is bound by the rhythm of seasons. Most people work the land with hand tools, and knowledge is passed down in families. The biggest disruption? Crop failures or a new tool like the seed drill."
    },
    "1800": {
        "factory": "In 1800, working in a factory means long shifts by steam-powered machines. Cities grow, coal smoke fills the air, and society debates child labor and workers’ rights. Discipline and routine dominate life."
    },
    "2000": {
        "software": "In 2000, as a software engineer, you’re part of the dot-com boom. Offices run on Windows, internet cafes pop up, and coding is becoming a global skill. The Y2K bug was your generation’s warm-up for modern software crises."
    },
    "2025": {
        "ai": "In 2025, as an AI product manager, your job is guiding agents and copilots. Machines do heavy lifting, but you shape the problems and keep humans in the loop. Prompting, ethics, and strategy are your new toolbox."
    },
}

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        year = request.form.get("year")
        job = request.form.get("job").lower()
        story = stories.get(year, {}).get(job)

        if story:
            return render_template("result.html", year=year, job=job, story=story)
        else:
            return render_template("result.html", year=year, job=job, story="Hmm… I don’t have a story for that combination yet. Try another year or job.")
    return render_template("index.html")
