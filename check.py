import requests
import smtplib
from email.message import EmailMessage
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

# Website List
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

# Headers
headers = {
    "User-Agent": "Mozilla/5.0"
}


# Send Mail Function
def send_mail(subject, body):

    try:

        msg = EmailMessage()

        msg['Subject'] = subject
        msg['From'] = EMAIL
        msg['To'] = TO_EMAIL

        msg.set_content(body)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

            smtp.login(EMAIL, PASSWORD)
            smtp.send_message(msg)

        print("Mail Sent Successfully")

    except Exception as e:

        print("Mail Sending Failed")
        print(e)


# Website Checking Function
def check_websites():

    working_sites = []
    failed_sites = []

    for site in websites:

        try:

            response = requests.get(
                site,
                headers=headers,
                timeout=15
            )

            if response.status_code == 200:

                working_sites.append(
                    f"{site} --> WORKING PROPERLY (200 SUCCESS)"
                )

            else:

                failed_sites.append(
                    f"{site} --> FAILED ({response.status_code})"
                )

        except requests.exceptions.Timeout:

            failed_sites.append(
                f"{site} --> TIMEOUT ERROR"
            )

        except requests.exceptions.ConnectionError:

            failed_sites.append(
                f"{site} --> CONNECTION ERROR"
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

        body += "\nFailed Websites:\n\n"

        for site in failed_sites:
            body += site + "\n"

        send_mail(
            "Website Failure Alert",
            body
        )

    print("Website Checking Completed")


# Run Function
check_websites()