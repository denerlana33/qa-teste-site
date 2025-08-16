from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_formulario_mensagem_erro():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("file:///C:/Users/Dener/OneDrive/Área%20de%20Trabalho/Projeto/qa-teste-site/index.html")

    # Clica em "Enviar" sem preencher nada
    submit_btn = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
    submit_btn.click()
    time.sleep(1)

    erro = driver.find_element(By.ID, "erro").text
    assert erro == "Todos os campos são obrigatórios."

    driver.quit()

def test_formulario_sucesso():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("file:///C:/Users/Dener/OneDrive/Área%20de%20Trabalho/Projeto/qa-teste-site/index.html")

    driver.find_element(By.ID, "nome").send_keys("Dener")
    driver.find_element(By.ID, "email").send_keys("dener@example.com")
    driver.find_element(By.ID, "mensagem").send_keys("Olá, isso é um teste!")

    submit_btn = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
    submit_btn.click()
    time.sleep(1)

    erro = driver.find_element(By.ID, "erro").text
    assert erro == ""

    driver.quit()
