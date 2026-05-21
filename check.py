import os
import requests
import smtplib
from email.message import EmailMessage
from datetime import datetime

websites = [
    "https://ishaatrends.com",
    "https://dhuniya.in",
    "https://ishustore.com",
    "https://www.schoolfirst.ai/",
    "https://www.familifirst.com/",
    "https://thesru.com/",
    "https://www.iqrartimes.com/",
    "https://www.anandads.com/",
    "https://www.paranpara.com/",
    "https://thesapphirehouse.in/",
    "https://main.d27jal83ewuisw.amplifyapp.com/",
    "https://orukal.com/"
]

# Render Environment Variables
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")


def send_mail(subject, body):

    msg = EmailMessage()

    msg['Subject'] = subject
    msg['From'] = EMAIL
    msg['To'] = TO_EMAIL

    msg.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL, PASSWORD)
        smtp.send_message(msg)


working_sites = []
failed_sites = []

for site in websites:

    try:

        response = requests.get(site, timeout=10)

        if response.status_code == 200:

            working_sites.append(
                f"{site} --> WORKING PROPERLY (200 SUCCESS)"
            )

        else:

            failed_sites.append(
                f"{site} --> FAILED ({response.status_code})"
            )

    except Exception as e:

        failed_sites.append(
            f"{site} --> ERROR ({str(e)})"
        )


current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# SUCCESS MAIL
if len(failed_sites) == 0:

    body = f"""
All Websites Are Working Properly

Time: {current_time}

Website Status:

"""

    for site in working_sites:
        body += site + "\n"

    send_mail(
        "All Websites Working Properly",
        body
    )


# FAILURE MAIL
else:

    body = f"""
Website Failure Alert

Time: {current_time}

Working Websites:
"""

    for site in working_sites:
        body += site + "\n"

    body += "\nFailed Websites:\n"

    for site in failed_sites:
        body += site + "\n"

    send_mail(
        "Website Failure Alert",
        body
    )


print("Website Checking Completed")