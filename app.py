from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    student = {
        "name": "Dasthagiri",
        "scores": [78, 85, 90, 92],
        "subjects": ["Math", "Science", "English", "CS"],
        "attendance": "92%"
    }
    tips = "Study one hour every day. Use flashcards and quizzes to remember better."
    quote = "Push yourself, because no one else is going to do it for you."

    return render_template("dashboard.html", student=student, scores=student["scores"],
                           subjects=student["subjects"], attendance=student["attendance"],
                           tips=tips, quote=quote)

# Needed for Render
import os
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
