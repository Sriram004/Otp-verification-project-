from flask import Flask, render_template, request, redirect, url_for, session, flash
import random
import smtplib
import ssl
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        email = request.form["email"]
        otp = str(random.randint(100000, 999999))

        # Send email
        message = f"""Subject: Your OTP Code

Your OTP code is: {otp}
It is valid for 3 minutes.
"""
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(SENDER_EMAIL, SENDER_PASSWORD)
                server.sendmail(SENDER_EMAIL, email, message)

            session["email"] = email
            session["otp"] = otp
            flash("OTP sent to your email.", "info")
            return redirect(url_for("verify"))

        except Exception as e:
            flash(f"Failed to send OTP: {e}", "danger")

    return render_template("index.html")

@app.route("/verify", methods=["GET", "POST"])
def verify():
    if request.method == "POST":
        user_otp = request.form["otp"]
        if user_otp == session.get("otp"):
            flash("OTP verified successfully!", "success")
            return redirect(url_for("index"))
        else:
            flash("Incorrect OTP. Please try again.", "danger")

    return render_template("verify.html")

if __name__ == "__main__":
    app.run(debug=True)
