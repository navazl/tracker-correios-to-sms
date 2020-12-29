import requests
from bs4 import BeautifulSoup

#settings


def scraping_cor(codnumber):
  #settings
  url = f'https://www.linkcorreios.com.br/?id={codnumber}'
  # url + request
  r_cor = requests.get(url)
  # salva o html no html_cor
  r_cor.encoding = r_cor.apparent_encoding
  #faz a sopa
  soup = BeautifulSoup(r_cor.text, 'html.parser')
  #filtrar o card 
  card_principal = soup.find('div', class_="card-header")
  #caça os status
  status = card_principal('ul', class_="linha_status m-0")

  #imprime os status final
  final_status = ''
  for statu in status:
    final_status += f'{statu.get_text()}'

  return final_status
