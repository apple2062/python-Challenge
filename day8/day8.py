import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"

#Goes to http://www.alba.co.kr and scrapes the companies on the front page.
#Then go to the page of each company and scrape each job.
#Create a .csv file for each company and write the jobs on it.
#제목 : 회사이름.csv((주)노랑통닭.csv)
#내용: place, title, time, pay, date(22분전 ,, 뭐이런식)
#근데 내용은 브랜드별 각 사이트 들어가지 않아도 나와있네..!
#(서울 구로구 , 노랑통닭 인천 주안점, 시간, "월급 20000000원", 33분전)

def save_to_file(informations,brand_name):
  file = open(f"{brand_name}.csv", mode = "w")
  writer = csv.writer(file)
  writer.writerow(["place","title","time","pay","date"])
  for info in informations:
    writer.writerow(list(info.values()))
  print(f"{brand_name}.csv 저장 완료!")


#알바천국은, indeed 처럼 메인 페이지가 여러페이지가 아니므로, get_last_page 를 구할 필요 없음
def brand_info(url,formalname):
  #http://lotteria.alba.co.kr/job/brand/?page={ }&pagesize={50}
  for brand_url in url:
    informations = []
    formal_name = formalname[url.index(brand_url)]
    print(brand_url)

    company = requests.get(brand_url)
    soup_company = BeautifulSoup(company.text,"html.parser")
    company_results = soup_company.find("div",{"id":"NormalInfo"}).find("tbody").find_all("tr")
    if len(company_results)==1:
      print("채용하는 정보 없습니다.")
    else:
      for tr in company_results:
        try:
          company_result = tr.find_all("td")
          company_name = tr.find("span",{"class":"company"}).text #(주)노랑통닭
          company_place = company_result[0].text # 서울 서초구
          company_time = company_result[2].text #9:00~18:00
          company_pay = company_result[3].text #시급 8590원
          company_date= company_result[4].text #4일전

        except:
          #print("summaryView")
          pass

        else:
          informations.append({'place':company_place,'title':company_name,'time':company_time,'pay':company_pay,'date':company_date})


    save_to_file(informations,formal_name)

def extract_brands(): # 브랜드마다 지정된 a href 가져와서 출력하는 작업
  brand_urls = []
  brand_formalname = []
  result_albas = requests.get(alba_url)
  soup_albas = BeautifulSoup(result_albas.text,"html.parser")
  brand_results = soup_albas.find("div",{"id":"MainSuperBrand"}).find_all("a",{"class":"goodsBox-info"})
  for i in brand_results:
    brand_formalname.append(i.find("span",{"class":"company"}).text)
    brand_urls.append(i['href']) #브랜드 별 url 주소

  brand_info(brand_urls,brand_formalname)
  
extract_brands()
