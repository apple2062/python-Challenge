import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency


"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""

#"Welcome to CurrencyConvert PRO 2000"

#"Where are you from? Choose a country by number" > #:
#"Now chosse another country" > #:
#"How many {COP} do tou want to convert to {KRW}?"
# > "That wasn't a number" / "{COP} { } is {}원"

#After getting the countries and their codes let the user choose two countries.
#Then let the user write an amount of currency 
#Then send the two currency codes and the amounts to a URL
# >https://transferwise.com/gb/currency-converter/gbp-to-usd-rate?amount=50

os.system("clear")
url1 = "https://www.iban.com/currency-codes"


result1 = requests.get(url1)
soup1 = BeautifulSoup(result1.text, "html.parser")
country = []

print("Welcome to CurrencyConvert PRO 2000")

def transferwise(money):
  url2 = f"https://transferwise.com/gb/currency-converter/{country[50][1].lower()}-to-{country[126][1].lower()}-rate?amount={money}"
  result2 = requests.get(url2)
  soup2 = BeautifulSoup(result2.text,"html.parser")
  amount = soup2.find("div",{"class":"col-lg-6 text-xs-center text-lg-left"}).find("span",{"class":"text-success"}).string
  return float(amount)*money


def converting(first,second):
  print(f"How many {country[first][1]} do you want to convert to {country[second][1]}?")
  try:
    convert_money = int(input())
  except:
    print("That wasn't a number")
    converting(first,second)
  else:
    reslut_converting = transferwise(convert_money)
    result_formatting = format_currency(reslut_converting, "KRW", locale="ko_KR")
    print(f"{country[first][1]} {convert_money} is {result_formatting}")

tb = soup1.find("tbody")
tr = tb.find_all('tr')
for i in tr:
  find_country = i.find_all('td')
  #code 가 none 값인 경우
  if find_country[1].string == "No universal currency":
    continue
  country.append((find_country[0].string.capitalize(),find_country[2].string))
for idx,val in enumerate(country):
  print(f'# {idx+1} {val[0]}')

print("Where are you from? Choose a country by number")

country_first = int(input("#: "))
print(f"{country[country_first][0]}")


print("Now choose another country")
country_second = int(input("#:"))
print(f"{country[country_second][0]}")

converting(country_first,country_second)


