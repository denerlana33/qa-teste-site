from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Inicia o navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # 🟢 CAMINHO LOCAL CORRETO PARA O ARQUIVO HTML
    driver.get("file:///C:/Users/Dener/OneDrive/Área%20de%20Trabalho/Projeto/qa-teste-site/qa-teste-site/formulario.html")


    # Espera até o campo 'nome' aparecer
    wait = WebDriverWait(driver, 10)
    nome_input = wait.until(EC.presence_of_element_located((By.ID, "nome")))

    # Preenche o campo
    nome_input.send_keys("Dener")

    # Espera 5 segundos para você ver o resultado
    time.sleep(5)

finally:
    driver.quit()
