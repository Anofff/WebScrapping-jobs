# Importing Libraries
import datetime
import time
import csv
from bs4 import BeautifulSoup
import requests
import smtplib
import os  # For environment variables

def find_jobs():
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="
    
    try:
        source = requests.get(url, headers=header)
        source.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    soup = BeautifulSoup(source.text, "html.parser")
    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")
    
    new_jobs = False  # To check if new jobs were posted recently

    # Writing the header only if the file is being created
    file_exists = os.path.exists("Job_info.csv")
    
    for job in jobs:
        published_date = job.find("span", class_="sim-posted").span.text.replace("  ", "")
        if "few" in published_date:
            company_name = job.find("h3", class_="joblist-comp-name").text.strip()
            application_link = job.header.h2.a["href"]
            required_skills = job.find("span", class_="srp-skills").text.strip()
            today = datetime.date.today()

            # Check if file exists to avoid rewriting headers each time
            with open("Job_info.csv", "a+", newline="", encoding="UTF8") as f:
                writer = csv.writer(f)
                if not file_exists:
                    writer.writerow(["Today", "Company Name", "Required Skills", "Application Link"])  # Writing header once
                writer.writerow([today, company_name, required_skills, application_link])

            new_jobs = True  # If new jobs are found

    if new_jobs:
        send_mail()


def send_mail():
    # Fetch email and password from environment variables for security reasons
    EMAIL_ADDRESS = os.getenv("EMAIL_USER")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASS")

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.ehlo()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        
        subject = "Python Job Posting!"
        body = "Your dream python job has been posted. Check the CSV file or the TimesJobs website."
        msg = f"Subject: {subject}\n\n{body}"

        recipient_email = input("Enter your email Address.Eg info@gmail.com")  
        server.sendmail(EMAIL_ADDRESS, recipient_email, msg)
        server.quit()

        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")


if __name__ == "__main__":
    while True:
        find_jobs()
        time.sleep(86400)  
