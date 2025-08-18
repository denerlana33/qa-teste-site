from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class FormularioPage:
    def __init__(self, driver):
        self.driver = driver

    def preencher_nome(self, nome):
        nome_input = self.driver.find_element(By.ID, "nome")
        nome_input.send_keys(nome)

    def preencher_email(self, email):
        email_input = self.driver.find_element(By.ID, "email")
        email_input.send_keys(email)

    def preencher_mensagem(self, mensagem):
        mensagem_input = self.driver.find_element(By.ID, "mensagem")
        mensagem_input.send_keys(mensagem)

    def clicar_enviar(self):
        botao_enviar = self.driver.find_element(By.ID, 'btn-enviar')
        botao_enviar.click()

    def obter_mensagem_erro(self):
        try:
            return self.driver.find_element(By.ID, "erro").text
        except NoSuchElementException:
            return None
