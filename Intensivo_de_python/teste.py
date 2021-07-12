from selenium import webdriver
import time

browser = webdriver.Firefox()

from datetime import date, timedelta

# 1 de janeiro de 2019
d = date(2019, 1, 1)


contador = 1
while True:
    d = d + timedelta(days=contador)
    url = f"https://www.bcb.gov.br/api/relatorio/sitebcb/txjuros?path=conteudo/decap/Reports/BoletimDiarioReport.rdl" \
          f"&parametros=%27DataBoletim:{d}%27&exportar=PDFRETRATO&nome=Di%C3%A1rio%20Eletr%C3%B4nico%{d}"
    browser.get(url)
    print("Arquivo baixado")
    contador += 1
    time.sleep(13)
