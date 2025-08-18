from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time  # ✅ IMPORTAÇÃO NOVA

from pages.formulario_page import FormularioPage


def test_preencher_formulario():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Caminho correto para o formulario.html que está na RAIZ
        caminho = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'formulario.html'))
        url = f"file:///{caminho.replace(os.sep, '/')}"
        print("Abrindo arquivo:", url)

        driver.get(url)

        # Aguarda o campo email aparecer
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "email"))
        )

        # Usa o Page Object para preencher
        pagina = FormularioPage(driver)
        pagina.preencher_nome("Dener")
        pagina.preencher_email("dener@email.com")
        pagina.preencher_mensagem("Mensagem de teste.")
        pagina.clicar_enviar()

        # ✅ Adicionados:
        print("✅ Botão Enviar foi clicado com sucesso!")
        time.sleep(5)  # Deixa o navegador aberto por 5 segundos

    finally:
        driver.quit()
