from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

def test_formulario_vazio_exibe_erro():
    print("🚨 Testando validação de campos vazios...")
    
    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("file:///C:/Users/Dener/OneDrive/Área%20de%20Trabalho/Projeto/qa-teste-site/index.html")

    time.sleep(1)

    botao = driver.find_element(By.TAG_NAME, "button")
    botao.click()

    time.sleep(1)

    mensagem_erro = driver.find_element(By.ID, "mensagem-erro").text
    assert mensagem_erro == "Todos os campos são obrigatórios!"

    print("✅ Validação de erro testada com sucesso.")
    driver.quit()
