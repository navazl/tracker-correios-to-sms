from flask import Flask, render_template, request, send_file
from scraping import scraping_cor
from sms_sender import sms

app = Flask("Correios")

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/enviado')
def enviado():
  codnumber = request.args.get('codnumber')
  telnumber = request.args.get('telnumber')
  scraping = scraping_cor(codnumber)
  sms(telnumber, codnumber, scraping)
  return render_template('enviado.html')

app.run(host='0.0.0.0')