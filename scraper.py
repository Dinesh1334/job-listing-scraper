import requests
from bs4 import BeautifulSoup
import pandas as pd

# Target URL
url = "https://realpython.github.io/fake-jobs/"

# Send GET request
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract job elements
jobs = soup.find_all("div", class_="card-content")

# Prepare data
job_list = []
for job in jobs:
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()
    link = job.find_all("a")[1]["href"]
    
    job_list.append({
        "Title": title,
        "Company": company,
        "Location": location,
        "Apply Link": link
    })

# Save to CSV
df = pd.DataFrame(job_list)
df.to_csv("job_listings.csv", index=False)

print("Scraping complete. Data saved to job_listings.csv")
