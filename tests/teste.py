print("Script Python rodando com sucesso!")

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("Abrindo o navegador...")

driver = webdriver.Chrome()
driver.get("https://www.google.com")

print("Navegador aberto com sucesso!")

time.sleep(5)  # Espera 5 segundos para você ver a janela

driver.quit()
print("Navegador fechado.")
