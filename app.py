from flask import Flask, render_template, request

app = Flask(__name__)

JOBS = ["farmer", "factory", "teacher", "software", "ai_pm"]
CENTURIES = ["1700", "1800", "1900", "2000", "2100"]

stories = {
    "1700": {
        "farmer": "1700 • Farmer: Your calendar is the sky. You trade hay for gossip and survival tips. Tools: hand plow, strong back, suspiciously optimistic neighbor. Pro tip: rotate crops, not excuses.",
        "factory": "1700 • Factory Worker: Factories aren’t quite the thing yet. You’re ‘pre-factory,’ which is a polite way to say ‘apprentice with sore wrists.’ Learn a craft and avoid sawdust in your tea.",
        "teacher": "1700 • Teacher: You herd tiny philosophers who ask ‘Why?’ 19 times per minute. Blackboard? Chalk? Luxury. You teach letters, numbers, and ‘please stop poking the goat.’",
        "software": "1700 • Software Engineer: You refactor… parchment. Your backlog is ‘invent electricity, then computers.’ Until then, you optimize loops in your head and brag about O(oxen).",
        "ai_pm": "1700 • AI PM: You pitch ‘automated thinking machines.’ Audience nods, then asks if it can also churn butter. Visionary, but maybe ship a better wheel first."
    },
    "1800": {
        "farmer": "1800 • Farmer: Steel plows, bigger yields, bigger hats. Markets expand; so do weeds. You discover logistics: move grain before rain. KPI: cows milked ÷ boots ruined.",
        "factory": "1800 • Factory Worker: Steam says ‘tick tock.’ You master the machine and invent the coffee break by glaring at supervisors. Join a union; keep your fingers.",
        "teacher": "1800 • Teacher: New schools! New rules! You teach handwriting so sharp it could slice bread. Parents debate modernity; you assign more homework.",
        "software": "1800 • Software Engineer: You and Ada dream in gears. Debugging means fewer cogs on the floor. ‘Hello, World’ is a loom that doesn’t jam.",
        "ai_pm": "1800 • AI PM: You storyboard a steam-powered assistant that schedules your boss’s nap. It ships as a kettle. Adoption is 100%; it makes tea."
    },
    "1900": {
        "farmer": "1900 • Farmer: Tractors arrive, horses negotiate early retirement. You read weather maps like stock charts. Pest control strategy: ‘Not today, locusts.’",
        "factory": "1900 • Factory Worker: Assembly lines turn walking into standing. You time motions like a metronome and stash earplugs made of courage.",
        "teacher": "1900 • Teacher: You wield the red pen of destiny. Students learn civics, science, and how to resist passing notes the size of newspapers.",
        "software": "1900 • Software Engineer: Punched cards everywhere. You drop a stack once and reinvent chaos theory. Unit tests are interns with rulers.",
        "ai_pm": "1900 • AI PM: You promise a thinking machine; you ship a very polite calculator. It can’t love, but it can sum. Management applauds anyway."
    },
    "2000": {
        "farmer": "2000 • Farmer: GPS tractors drift like techno-ballet. Drones scout fields; spreadsheets judge you. You A/B test fertilizer like a startup.",
        "factory": "2000 • Factory Worker: Robots join the crew; you learn maintenance and meme curation. Kaizen boards multiply like… well, kaizen boards.",
        "teacher": "2000 • Teacher: Projectors! Wi-Fi! Also: 37 passwords. You teach critical thinking and how to find the real ‘Submit’ button.",
        "software": "2000 • Software Engineer: You deploy to prod on Friday (brave). Pager beeps become your love language. Version control: finally not zip files.",
        "ai_pm": "2000 • AI PM: You ship search, recommenders, and the ‘Are you a robot?’ checkbox. Answer remains unclear."
    },
    "2100": {
        "farmer": "2100 • Farmer: Vertical farms hum; tomatoes grow next to servers. You tune nutrients like a DJ. Pests now subscribe to your patch notes.",
        "factory": "2100 • Factory Worker: Cobots high-five (safely). You choreograph fleets and argue with a forklift that wants a vacation.",
        "teacher": "2100 • Teacher: Your class includes humans, AIs, and one curious cat avatar. You grade reflections; the rubric grades itself.",
        "software": "2100 • Software Engineer: You pair program with an agent that apologizes for merge conflicts it caused in 2087. Code smells are now scented.",
        "ai_pm": "2100 • AI PM: You run governance, deploy planetary updates, and ensure ‘Don’t be a villain’ is more than a slide. KPIs: trust, uptime, no dystopia."
    }
}

def safe_lower(x): return (x or "").strip().lower()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        century = request.form.get("century")
        job = safe_lower(request.form.get("job"))
        story = stories.get(century, {}).get(job)
        if not story:
            story = "No story for that combo (yet). Try another!"
        return render_template("result.html", century=century, job=job, story=story, JOBS=JOBS, CENTURIES=CENTURIES)
    return render_template("index.html", JOBS=JOBS, CENTURIES=CENTURIES)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
