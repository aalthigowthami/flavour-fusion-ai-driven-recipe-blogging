
import os
import random
from flask import Flask, render_template, request
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

app = Flask(__name__)

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why was the computer cold? It forgot to close its Windows!",
    "Why do Java developers wear glasses? Because they don’t C#!"
]

@app.route("/", methods=["GET", "POST"])
def index():
    blog_content = ""
    joke = ""

    if request.method == "POST":
        topic = request.form["topic"]
        word_count = request.form["word_count"]

        prompt = f"Write a detailed recipe blog on {topic} in approximately {word_count} words."

        response = model.generate_content(prompt)
        blog_content = response.text
        joke = random.choice(jokes)

    return render_template("index.html", blog=blog_content, joke=joke)

if __name__ == "__main__":
    app.run(debug=True)
