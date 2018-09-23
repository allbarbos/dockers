from bs4 import BeautifulSoup
import requests

r = requests.get('https://www.al.sp.gov.br/alesp/deputados-estaduais/')
soup = BeautifulSoup(r.text, 'lxml')
print(soup)