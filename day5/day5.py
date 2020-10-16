import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"

# gets a list of countries from a website with their currency codes
# let the user choose a country and display the currency code of that country.

# Save the name of the country and the "Alpha-3 code" in an array.
# Some countries don't have currency (No universal currency), don't add them to the list.
# Check the user input, only numbers from inside the country list are allowed.
# When a country is selected, show the name and currency code.
# Use try/except when converting strings to numbers. ( int(input()) )

# Hello! Please choose select a country by number: #처음
# That wasn't a number. #이상한 숫자아닌 단어 입력 시
# Choose a number from the list. #크롤링한 숫자 안에 속하지 않을 때
# You choose {} / The currency node is {}

result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")
country = []
code = []
country_number = []

def check_invalid():
  try:
    number = input("#:")
    number = int(number)
  except:
    print("That wasn't a number.")
    check_invalid()
  else:
    if number in country_number:
      print(f"You choose {country[number-1][0]} \nThe currency node is {country[number-1][1]}")
    else:
      print("Choose a number from the list.")
      check_invalid()
tb = soup.find("tbody")
tr = tb.find_all('tr')
idx = 1
for i in tr:
  find_country = i.find_all('td')
  #code 가 none 값인 경우
  if find_country[1].string == "No universal currency":
    continue
  country.append((find_country[0].string.capitalize(),find_country[2].string))
  country_number.append(idx)
  #print(find_country[0].string.capitalize(),find_country[2].string ,idx, country.index(find_country[0].string.capitalize()))
  idx += 1
print(country[0])
print(country_number)

print("Hello! Please choose select a country by number:")
for idx,val in enumerate(country):
  print(f'# {idx+1} {val[0]}')

check_invalid()
