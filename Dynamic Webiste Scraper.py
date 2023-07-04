from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from bs4 import BeautifulSoup
import time

url = "https://www.naukri.com/top-jobs-by-designations#desigtop600"

options = Options()
options.use_chromium = True
options.add_argument("start-maximized")

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)
driver.get(url)

time.sleep(5)

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")
all_divs = soup.find('div', {'id': 'nameSearch'})
job_profiles = all_divs.find_all('a')


count = 0
for job_profile in job_profiles:
    print(job_profile.text)
    count += 1
    if count == 10:
        break

driver.quit()
