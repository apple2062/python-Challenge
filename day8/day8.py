import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"
MAX_PAGE_SIZE = 1500 #브랜드별 몇개의 정보를 파일로 저장할 것인지 변수 지정

def save_to_file(informations,brand_name):
  file = open(f"{brand_name}.csv", mode = "w")
  writer = csv.writer(file)
  writer.writerow(["place","title","time","pay","date"])
  for info in informations:
    writer.writerow(list(info.values()))
  print(f"{brand_name}.csv 저장 완료!")


#알바천국은, indeed 처럼 메인 페이지가 여러페이지가 아니므로, get_last_page 를 구할 필요 없음
def brand_info(url,formalname):
  for brand_url in url:
    #brand_url = http://lotteria.alba.co.kr/
    #url_for_parse = http://lotteria.alba.co.kr/job/brand/?page=1&pagesize={}
    informations = []
    url_for_parse = brand_url + f'job/brand/?page=1&pagesize={MAX_PAGE_SIZE}'

    print(url_for_parse)

    formal_name = formalname[url.index(brand_url)]
    company = requests.get(url_for_parse)
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