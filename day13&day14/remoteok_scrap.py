import requests
from bs4 import BeautifulSoup

url = "https://remoteok.io/remote-dev+"

def scrap_jobs(word):
  remoteok_jobs = []
  try:
    html = requests.get(f"{url}{word}-jobs").text
    soup = BeautifulSoup(html,"html.parser")
    if soup.find('table',{"id":"jobsboard"}):
      jobs = soup.find('table',{"id":"jobsboard"}).find_all('tr',{"class":"job"})
      for job in jobs:
        job_title = job.find('td',{'class':'company'}).find('h2').text
        job_company = job.find('td',{'class':'company'}).find('h3').text
        job_link = job.find('td',{'class':'company'}).find('a',{'class':'preventLink'})['href']
        job_info = {
          'title': job_title,
          'company': job_company,
          'link': f"https://remoteok.io/{job_link}"
        }
        remoteok_jobs.append(job_info)
    return remoteok_jobs
  except:
    return []