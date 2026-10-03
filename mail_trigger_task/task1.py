import smtplib
from email.message import EmailMessage

# -----------------------------
# EMAIL DETAILS
# -----------------------------

SENDER_EMAIL =nazriya6.k@gmail.com"
APP_PASSWORD = "tgcqxnycqejiekkk"
RECEIVER_EMAIL = "luckypottik2019@gmail.com"


# -----------------------------
# TEST
# -----------------------------

try:
    print("Running program...")

    # This is our test
    number = 10
    result = number / 3

    # If the above works, SUCCESS
    status = "PASS"
    message = f"""
Python Test Result: PASS

The program ran successfully.

Result: {result}
"""

except Exception as e:

    # If something goes wrong, ERROR
    status = "FAIL"
    message = f"""
Python Test Result: FAIL

Error Type: {type(e).__name__}
Error Reason: {str(e)}
"""


# -----------------------------
# SEND EMAIL
# -----------------------------

email = EmailMessage()

email["From"] = SENDER_EMAIL
email["To"] = RECEIVER_EMAIL
email["Subject"] = f"Python Test - {status}"

email.set_content(message)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(SENDER_EMAIL, APP_PASSWORD)
    smtp.send_message(email)

print("Email sent successfully!")
print(status)

