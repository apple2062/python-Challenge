import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/jobs?r=true"

def get_last_page(word):
  html = requests.get(f"{url}&q={word}").text
  soup = BeautifulSoup(html,"html.parser")
  if soup.find('div',{"class":"s-pagination"}):
    pages = soup.find('div',{"class":"s-pagination"}).find_all('span')
    return int(pages[-2].text)
  else:
    return 1;

def scrap_jobs(word):
  stack_jobs = []
  try:
    last_page = get_last_page(word)
    for page in range(last_page):
      html = requests.get(f"{url}&q={word}&pg={page+1}").text
      soup = BeautifulSoup(html,"html.parser")
      if soup.find('div',{'class':'s-empty-state wmx4 p48 ta-center'}):
        raise Exception()
      if soup.find('div',{"class":"listResults"}):
        jobs = soup.find('div',{"class":"listResults"}).find_all('div',{"class":"-job"})
        for job in jobs:
          job_title = job.find('a',{'class':'s-link'}).text
          job_company = job.find('h3').find('span').text.strip()
          job_link = job.find('a',{'class':'s-link'})['href']
          job_info = {
            'title': job_title,
            'company': job_company,
            'link': f"https://stackoverflow.com{job_link}"
          }
          stack_jobs.append(job_info)
    return stack_jobs
  except:
    return []
