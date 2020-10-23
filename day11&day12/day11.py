import requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup

"""
When you try to scrape reddit make sure to send the 'headers' on your request.
Reddit blocks scrappers so we have to include these headers to make reddit think
that we are a normal computer and not a python script.
How to use: requests.get(url, headers=headers)
"""

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


"""
All subreddits have the same url:
i.e : https://reddit.com/r/javascript
You can add more subreddits to the list, just make sure they exist.
To make a request, use this url:
https://www.reddit.com/r/{subreddit}/top/?t=month
This will give you the top posts in per month.
"""

subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django"
]



app = Flask("DayEleven")

db = {}
subreddits_info = {}


@app.route("/")
def home():
  return render_template(
    "home.html",
    subreddits = subreddits
  )


@app.route("/read")
def read():
  for subreddit in db.keys():
    if request.args.get(subreddit) == "on":      
      db[subreddit] = subreddit
    
  if db =={}:
    for subreddit in subreddits:
      on = request.args.get(subreddit)
      if on == "on":
        subreddits_info[subreddit] = []
        url = f"https://www.reddit.com/r/{subreddit}/top/?t=month"
        result = requests.get(url, headers=headers)
        soup = BeautifulSoup(result.text, "html.parser")
        posts = soup.find_all("div",{"class":"_1oQyIsiPHYt6nx7VOmd1sz"})
        for post in posts:
          title = post.find("h3",{"class":"_eYtD2XCVieq6emjKBH3m"}).string
          link = post.find("a",{"class":"_3jOxDPIQ0KaOWpzvSQo-1s"})["href"]
          votes = post.find("div",{"class":"_1rZYMD_4xY3gRcSS3p8ODO"}).string
          subreddits_info[subreddit].append([title, link, votes])
          db[subreddit] = subreddits_info[subreddit]
  else:   
    for subreddit in db.values():
      subreddits_info[subreddit] = db[subreddit]

  return render_template(
    "read.html",
    subreddits = subreddits_info,
    subreddit_list = db.keys(),
  )

  

app.run(host="0.0.0.0")