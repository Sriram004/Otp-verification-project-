# 🔐 OTP Verification System using Python

This project is a simple and secure One-Time Password (OTP) verification system built in Python. It sends a randomly generated OTP to the user's email and validates the OTP entered by the user within a time limit.

---

## 🚀 Features

- ✅ Random 6-digit OTP generation
- 📧 Sends OTP via email (SMTP - Gmail)
- ⏰ OTP expiry time (3 minutes)
- 🔄 Allows up to 3 attempts for OTP entry
- 🔒 Uses `.env` file for secure credential management

---

## 🛠️ Tech Stack

- Python 3.x
- `smtplib`, `ssl`, `random`, `time` (standard)
- `python-dotenv` (for managing secrets)

---

## 🧪 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/otp-verification.git
cd otp-verification
2. Install dependencies
bash
Copy
Edit
pip install python-dotenv
3. Create .env file
Create a file named .env in the root directory and add your credentials:

env
Copy
Edit
SENDER_EMAIL=your_email@gmail.com
SENDER_PASSWORD=your_app_password
⚠️ For Gmail, enable 2-Step Verification and generate an App Password from:
https://myaccount.google.com/apppasswords

4. Run the program
bash
Copy
Edit
python otp_verifier.py
🧩 How It Works
You enter the recipient's email address.

A random 6-digit OTP is generated.

The OTP is sent via email using SMTP over SSL.

The user has 3 minutes and 3 attempts to enter the correct OTP.

On success or failure, a message is printed.

🗂️ File Structure
bash
Copy
Edit
otp-verification/
├── otp_verifier.py       # Main script
├── .env                  # Stores email credentials (not pushed to GitHub)
├── .gitignore            # Ignores .env and __pycache__
└── README.md             # Project documentation
⚠️ Security Tips
Never share your .env file or credentials publicly.

Use App Passwords instead of your real Gmail password.

Store secrets securely in production environments.

📄 License
This project is licensed under the MIT License.

🙋‍♂️ Author
Sriram Sowmyan
GitHub: Sriram004
LinkedIn: Sriram S

🌟 Star this repo if you found it useful!
yaml
Copy
Edit

---

Let me know if you'd like me to generate a `requirements.txt` or help you deploy it to Heroku or Replit.
