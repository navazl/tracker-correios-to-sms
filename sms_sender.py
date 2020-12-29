from twilio.rest import Client
from scraping import scraping_cor

# autenticacao twilio

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

def sms(telnumber, codigo, scraping):
  client.messages.create(
  to=telnumber,
  from_="",
  body=f"Sua encomenda {codigo} está com a ultima atualização como {scraping}"
)