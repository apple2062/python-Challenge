import requests
from flask import Flask, render_template, request , redirect
#Using this boilerplate we are going to build a mini clone of the 
#Hacker News Website(https://news.ycombinator.com/)
#using the Hacker News Search API(https://hn.algolia.com/api) and Flask.


#The website should have the following routes:
#/
#/?order_by=new
#/?order_by=popular
#/<id>

#Implement a fake DB like on the video #4.6 so 'new' and 'popular' can load faster.
#The template should reflect the current order_by selection.
#The main page "/" should by default order_by popular
#here should be a link to each of the stories to go and see the comments.

#<hint>
#If a comment does not have an author it means it has been deleted.
#To render the comment text, use the "safe" tag from Flask.
#Don't worry about the CSS, I have included "a .css file" on the boilerplate that will style the default HTML elements, just use <header> <section> <div><h1> etc and it will automatically look nice.(https://andybrewer.github.io/mvp/)
#The API has a limit of 10,000 requests per hour so don't go crazy and you will be alright.

base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"


db = {}
app = Flask("DayNine") #앱 이름 정하기

@app.route("/") #home 부분 (by default order_by popular)
def home():
  #order_by = request.args.get('order_by') or "popular" 이렇게 해봐! 
  # 그럼 / 일때(query string이 없을때) 
  #request.args.get("order_by") 가 None 이라서 default로 popular가 order_by에 저장 될 것이다.
  order = request.args.get('order_by') or 'popular'
  if order == "new":
    order_result = requests.get(new).json()
  elif order == "popular":
    order_result = requests.get(popular).json()
  else:
    redirect("/")
  print(type(order_result))
  hit = order_result['hits']
  db[order] = hit
  return render_template("index.html",hit =hit, order=order)

# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
@app.route("/<id>")
def make_detail_url(id):
  #/api/v1/items/16582136
  comment = f"{base_url}/items/{id}"
  comments = requests.get(comment).json()
  print(type(comments))
  return render_template("detail.html",result=comments) #변수명 result로 comments 데이터 들을 detail.html에 보낸다.

app.run(host="0.0.0.0")