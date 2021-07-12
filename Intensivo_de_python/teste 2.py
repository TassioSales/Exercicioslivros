from datetime import date, timedelta
from urllib.request import urlopen


def download_file(url):
    response = urlopen(url)
    cont = 0
    # 1 de janeiro de 2019
    d = date(2019, 1, 1)

    while True:
        d = d + timedelta(days=cont)
        with open(f"{d}.pdf", "wb") as file:
            file.write(response.read())
            print("Feito!!!")
        cont += 1


def main():
    # 1 de janeiro de 2019
    d = date(2019, 1, 1)

    contador = 0
    while True:
        d = d + timedelta(days=contador)
        url = f"https://www.bcb.gov.br/api/relatorio/sitebcb/txjuros?path=conteudo/decap/Reports/BoletimDiarioReport.rdl" \
              f"&parametros=%27DataBoletim:{d}%27&exportar=PDFRETRATO&nome=Di%C3%A1rio%20Eletr%C3%B4nico%{d}"
        download_file(url)
        contador += 1
        if contador == 502:
            break


main()
