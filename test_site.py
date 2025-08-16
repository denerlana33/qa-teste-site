from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_conteudo_html():
    caminho_arquivo = "file:///C:/Users/Dener/OneDrive/Área%20de%20Trabalho/Projeto/qa-teste-site/index.html"

    driver = webdriver.Chrome()
    driver.get(caminho_arquivo)
    time.sleep(2)

    h1 = driver.find_element(By.TAG_NAME, "h1")
    assert "Bem-vindo ao Projeto de Testes QA" in h1.text

    itens = driver.find_elements(By.TAG_NAME, "li")
    assert len(itens) == 3

    link = driver.find_element(By.TAG_NAME, "a")
    assert link.get_attribute("href") == "https://github.com/denerlana33/qa-teste-site"

    driver.quit()
