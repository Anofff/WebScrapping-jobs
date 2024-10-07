# Python Job Scraper from TimesJobs

This is a Python-based web scraping tool designed to scrape Python-related job postings from the TimesJobs website. The jobs are filtered based on postings made "a few days ago" and saved to a CSV file (`Job_info.csv`). Additionally, the script can send an email notification when new jobs are found.

## Features
- Scrapes Python-related jobs from [TimesJobs](https://www.timesjobs.com/).
- Saves job data (company name, skills, and application link) into a CSV file.
- Sends email notifications when new jobs are posted.
- Scheduled to run daily to check for the latest job postings.

## Technologies Used
- Python
- BeautifulSoup (for web scraping)
- Requests (for HTTP requests)
- CSV (for writing job data to a file)
- smtplib (for sending emails)

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- Virtual Environment (optional, but recommended)
- [Google App Password](https://support.google.com/accounts/answer/185833?hl=en) (required if using Gmail for email notifications)

## Setup

### 1. Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/yourusername/WebScrapping-jobs.git
