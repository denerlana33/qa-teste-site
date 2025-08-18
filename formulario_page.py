from selenium.webdriver.common.by import By

class FormularioPage:
    def __init__(self, driver):
        self.driver = driver

    def preencher_nome(self, nome):
        self.driver.find_element(By.ID, "nome").send_keys(nome)

    def preencher_email(self, email):
        self.driver.find_element(By.ID, "email").send_keys(email)

    def preencher_mensagem(self, mensagem):
        self.driver.find_element(By.ID, "mensagem").send_keys(mensagem)

    def clicar_enviar(self):
        self.driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

    def obter_mensagem_erro(self):
        return self.driver.find_element(By.ID, "erro").text
