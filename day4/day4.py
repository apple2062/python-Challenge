import requests
# with or without "http", "spaces", "uppercase" , "lowercase"
#> hello.com , kfjalkfa , jdfklaj, google.com
# >> "   " is up!
# >> "   " is down! 
# >> "  " is not a valid URL
# 이게 끝나면 유저는 프로그램 restart 가능 > Do you want start over? y/N 
# >> that's not a valid answer


 #try에서 판별하고 except에서 down. else에서 up
 #단순 url이 유효한지 유효하지 않은지만 판별,추가적인 코드라인은 필요없이
 #for 내부에 try-except를 넣는게 낫다
 
def add_http(url):
  if url[:4] != "http": #http로 시작하지 않을 때,
    url_modify = "http://"+url
    return url_modify
  else: #http 로 시작 할 때,#status code 확인
    return url

def yesno(startover):
    print("Do you want to start over? y/n")
    y_or_n = input()
    if y_or_n == 'n':
        startover = False
        print("k, Bye!")
        return startover
    elif y_or_n != 'y' and y_or_n != 'n':
        yesno(startover)
    else:
        return startover


print("Welcome to IsItDown.py!")

while True:  
    startover = True
    url_arr = []
    print("please wrute a URL or URLs you want to check. (seperated by comma)")
    urls = input().split(",")
    for i in urls:
        url_arr.append(add_http(i.strip()))
    
    for i in url_arr:
        try:
            r = requests.get(i)
            r.status_code
        except:
            print(f"{i} is down! ")
        else:
            print(f"{i} is up! ")
    startover = yesno(startover)
    if startover == False:
        break
    else:
        continue
        
    
    