import requests
from bs4 import BeautifulSoup
import json
import re
import time

# url = "https://www.work.ua/jobs-python/"

# headers = {
#     "Accept":"*/*",
#     "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Mobile Safari/537.36"
# }

# req = requests.get(url, headers=headers)
# src = req.text

# with open("index.html", "w", encoding="utf-8") as file:
#     file.write(src)

with open("index.html", "r", encoding="utf-8") as file1:
    src = file1.read()

soup = BeautifulSoup(src, "lxml")

jobs = []


info_job = soup.find_all("div", class_=["card-hover"])

for item in info_job:
    name_job = item.find("div", class_="mb-lg").find("h2", class_="my-0").find("a")
    price_job = item.find("span", class_="strong-600")
    company_job = item.find("div", class_="mt-xs").find("span", class_="strong-600")
    city_job = (item.find("span", class_="").find_parent("div", class_="mt-xs")).find_all("span", class_="")

    if price_job != None:
        if "грн" in price_job.text:
            price_job = re.sub(r"\s+", "", price_job.get_text())
        else:
            price_job = None

    jobs.append({
    "name" : name_job.text.strip(),
    "price" : price_job,
    "company" : company_job.text.strip(),
    "city" : city_job[-1].text.strip(", ").strip(),
    "link" : f"https://www.work.ua{name_job.get("href")}"
    })

with open("workua_python_jobs.json", "w", encoding="utf-8") as file2:
    json.dump(jobs, file2, ensure_ascii=False, indent=2)