from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

print("Script Python rodando com sucesso!")
print("Abrindo o navegador...")

# Caminho absoluto do index.html
caminho_arquivo = os.path.abspath("index.html")
url = "file://" + caminho_arquivo

# Inicializa o navegador
driver = webdriver.Chrome()

try:
    # Abre a página local
    driver.get(url)

    # Aguarda carregamento
    time.sleep(2)

    # Verifica o título da aba
    assert "Projeto de Testes QA" in driver.title
    print("✅ Título da página está correto.")

    # Verifica se o h1 contém o texto esperado
    h1 = driver.find_element(By.TAG_NAME, "h1")
    assert "Bem-vindo ao Projeto de Testes QA" in h1.text
    print("✅ Texto principal (h1) encontrado.")

    # Verifica se os 3 objetivos estão presentes
    objetivos = driver.find_elements(By.TAG_NAME, "li")
    assert len(objetivos) == 3
    print("✅ Lista de objetivos contém 3 itens.")

    # Verifica o link do GitHub
    link = driver.find_element(By.TAG_NAME, "a")
    assert "github.com/denerlana33/qa-teste-site" in link.get_attribute("href")
    print("✅ Link do GitHub está correto.")

except AssertionError as e:
    print("❌ Algum teste falhou:", e)

finally:
    time.sleep(2)
    driver.quit()
    print("Navegador fechado.")

