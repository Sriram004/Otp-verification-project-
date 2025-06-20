import smtplib
import ssl
import random
import time
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

def generate_otp():
    return str(random.randint(100000, 999999))

def send_email_otp(receiver_email, otp):
    message = f"""Subject: OTP Verification Code

Your OTP code is: {otp}
It is valid for 3 minutes.
"""
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, receiver_email, message)
        print(f"✅ OTP sent to {receiver_email}")
    except Exception as e:
        print("❌ Failed to send email:", e)
        exit()

def verify_otp(sent_otp, expiry_time):
    attempts = 3
    while attempts > 0:
        user_otp = input("Enter the OTP: ")

        if time.time() > expiry_time:
            print("❌ OTP expired!")
            return False

        if user_otp == sent_otp:
            print("✅ OTP verified successfully!")
            return True
        else:
            attempts -= 1
            print(f"❌ Incorrect OTP. {attempts} attempts left.")
    return False

def main():
    receiver_email = input("Enter your email: ")
    otp = generate_otp()
    expiry = time.time() + 180  # 3 minutes validity
    send_email_otp(receiver_email, otp)
    verify_otp(otp, expiry)

if __name__ == "__main__":
    main()
