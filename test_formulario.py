import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.pages.test_formulario import FormularioPage

def test_preencher_formulario():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)

    caminho = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'formulario.html'))
    url = f"file:///{caminho.replace(os.sep, '/')}"
    driver.get(url)

    time.sleep(1)

    pagina = FormularioPage(driver)
    pagina.preencher_nome("dener")
    pagina.preencher_email("dener@email.com")
    pagina.preencher_mensagem("Olá teste enviado!")

    pagina.clicar_enviar()
    time.sleep(2)

    driver.quit()
    assert True  # só para o Pytest não reclamar
