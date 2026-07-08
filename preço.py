from selenium import webdriver
import schedule
import time
from datetime import datetime

def pegar_preco():
    navegador = webdriver.Chrome()

    link = "https://www.google.com/travel/flights?tcfs=EiwKCC9tLzAzXzNkEgZKYXDDo28aGAoKMjAyNi0wNy0zMRIKMjAyNi0wOC0zMSIYCgoyMDI2LTA3LTMxEgoyMDI2LTA4LTMxUgRgAXgB&ved=0CAUQyJABahcKEwjoqYfL1LSVAxUAAAAAHQAAAAAQCA&ictx=2&tfs=CBwQARopEgoyMDI2LTA3LTMxag0IAhIJL20vMDIycGZtcgwIBBIIL20vMDNfM2QaKRIKMjAyNi0wOC0zMWoMCAQSCC9tLzAzXzNkcg0IAhIJL20vMDIycGZtQAFIAXABggELCP___________wGYAQE&tfu=KgIIBQ"
    navegador.get(link)

    time.sleep(5)

    preco = navegador.find_element("class name", "AdWm1c").text
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with open("preco.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{agora} - {preco}\n")

    navegador.quit()

schedule.every().hour.do(pegar_preco)

# roda uma vez logo ao iniciar, sem precisar esperar 1h pra primeira leitura
pegar_preco()

while True:
    schedule.run_pending()
    time.sleep(1)