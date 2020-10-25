"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""

import csv
from flask import Flask, request, render_template, redirect, send_file
from stackoverflow_scrap import scrap_jobs as stack_scrap_jobs
from wework_scrap import scrap_jobs as wework_scrap_jobs
from remoteok_scrap import scrap_jobs as remoteok_scrap_jobs

app = Flask("SearchJobs")
db = {}
recently_list = []

def get_all_jobs(word):
  all_jobs = []
  all_jobs = all_jobs + stack_scrap_jobs(word) + wework_scrap_jobs(word) + remoteok_scrap_jobs(word)
  return all_jobs

def save_to_db(word):
  fromdb = db.get(word)
  if fromdb:
    keyword_job = fromdb
  else:
    keyword_job = get_all_jobs(word)
    if not keyword_job:
      return []
    db[word] = keyword_job
  return keyword_job

def save_to_file(word,info):
  file = open(f"static/{word}.csv",mode="w")
  writer = csv.writer(file)
  writer.writerow([f"{word}"])
  writer.writerow(["title","company","link"])
  for job in info:
    writer.writerow(list(job.values()))


@app.route("/")
def home():
  return render_template("home.html",recently_list=recently_list)

@app.route("/jobs")
def jobs():
  field = request.args.get('field')
  if field:
    field = field.lower()
    post = save_to_db(field)
    if not post:
      return redirect('/error')
    else:
      if field not in recently_list:
        recently_list.append(field)
      return render_template('job.html',job_info=post,searched=field)
  else:
    return redirect('/error')

@app.route("/download.csv")
def download():
  file_name = request.args.get('file')
  if file_name:
    jobs_in_db = db.get(file_name)
    if not jobs_in_db:
      return redirect("/error")
    else:
      save_to_file(file_name,jobs_in_db)
      return send_file(f"static/{file_name}.csv",mimetype='text/csv')
  else:
    return redirect("/error")

@app.route("/error")
def error():
  return render_template("error.html")



app.run('0.0.0.0')