from flask import Flask, render_template
import os

app = Flask(__name__)

# ✅ AI Tip function
def get_study_tip(scores):
    avg = sum(scores) / len(scores)
    if avg >= 90:
        return "🎯 Excellent performance! Challenge yourself with advanced problems."
    elif avg >= 75:
        return "📘 Good job! Focus on weaker subjects to raise your average."
    elif avg >= 60:
        return "📈 You’re improving! Keep practicing and reviewing key topics."
    else:
        return "🔍 Time to revise basics. Study regularly and seek help when stuck."

# ✅ Route
@app.route("/")
def home():
    student = {
        "name": "Dasthagiri",
        "scores": [78, 85, 90, 92],
        "subjects": ["Math", "Science", "English", "CS"],
        "attendance": "92%"
    }

    tips = get_study_tip(student["scores"])
    quote = "Push yourself, because no one else is going to do it for you."

    return render_template("dashboard.html",
                           student=student,
                           scores=student["scores"],
                           subjects=student["subjects"],
                           attendance=student["attendance"],
                           tips=tips,
                           quote=quote)

# ✅ Required for Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
