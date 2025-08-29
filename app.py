import openai
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        year = request.form.get("year")
        job = request.form.get("job")

        # Call the model
        prompt = f"Write a rich, imaginative story about someone working as a {job} in the year {year}. Include social context, challenges, and what skills would matter over the next 25 years."

        response = openai.chat.completions.create(
            model="gpt-4o-mini",  # fast, cheap option
            messages=[{"role": "user", "content": prompt}],
        )

        story = response.choices[0].message.content
        return render_template("result.html", year=year, job=job, story=story)

    return render_template("index.html")
