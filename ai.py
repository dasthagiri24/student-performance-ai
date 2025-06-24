
def analyze_student(score, attendance):
    if score < 50 or attendance < 60:
        return "High Risk", "Focus on basics, attend classes regularly."
    elif score < 70 or attendance < 75:
        return "Medium Risk", "Revise weekly, improve time management."
    else:
        return "Low Risk", "Great job! Keep up the consistency!"
