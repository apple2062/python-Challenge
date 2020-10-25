import requests
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/remote-jobs/search?term="

def scrap_jobs(word):
  wework_jobs = []
  try:
    html = requests.get(f"{url}{word}").text
    soup = BeautifulSoup(html,"html.parser")
    if soup.find('div',{"class":"content"}):
      jobs = soup.find('div',{"class":"content"}).find('div',{"class":"jobs-container"}).find_all('li',{'class':['feature', '']})
      for job in jobs:
        job_title = job.find('a',recursive=False).find('span',{'class':'title'}).text
        job_company = job.find('a',recursive=False).find('span',{'class':'company'}).text
        job_link = job.find('a',recursive=False)['href']
        job_info = {
          'title': job_title,
          'company': job_company,
          'link': f"https://weworkremotely.com{job_link}"
        }
        wework_jobs.append(job_info)
    return wework_jobs
  except:
    return []
