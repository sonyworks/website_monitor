import requests
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# Websites list
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
    "https://orukal.com/",
]

# Email settings
sender_email = "sony@lifeboat.co.in"
app_password = "gulx piar hibe jxuz"

receiver_email = "sonycheviti@gmail.com"

# Store results
message = f"Website Status Report\nTime: {datetime.now()}\n\n"

for site in websites:
    try:
        response = requests.get(site, timeout=10)

        if response.status_code == 200:
            status = f"✅ SUCCESS - {site} is UP (200 OK)"
        else:
            status = f"❌ FAILED - {site} returned {response.status_code}"

    except Exception as e:
        status = f"❌ ERROR - {site} is DOWN\nReason: {e}"

    print(status)
    message += status + "\n"

# Send mail
msg = MIMEText(message)
msg["Subject"] = "Website Status Report"
msg["From"] = sender_email
msg["To"] = receiver_email

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, app_password)
    server.send_message(msg)
    server.quit()

    print("✅ Mail Sent Successfully")

except Exception as e:
    print("❌ Mail Sending Failed")
    print(e)