import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestAutenticacao(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/")  # Atualize com a URL correta


    def test_login_credenciais_invalidas(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Login").click()
        driver.find_element(By.NAME, "username").send_keys("usertest")
        driver.find_element(By.NAME, "password").send_keys("user123")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        erro = driver.find_element(By.CLASS_NAME, "alert-danger").text
        self.assertEqual(erro, "Credenciais inválidas")
        

        time.sleep(3)
    

    def test_redefinicao_senha_email_correto(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Login").click()
        driver.find_element(By.LINK_TEXT, "Esqueceu sua senha?").click()
        driver.find_element(By.NAME, "email").send_keys("user@teste.com")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        confirmacao = driver.find_element(By.CLASS_NAME, "alert-danger").text
        self.assertEqual(confirmacao, "Email de recuperação enviado!")

        time.sleep(3)
    
    def test_cadastro_usuario_existente(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Registrar").click()
        driver.find_element(By.NAME, "username").send_keys("aaa")
        driver.find_element(By.NAME, "email").send_keys("usuario@teste.com")
        driver.find_element(By.NAME, "password1").send_keys("aaa")
        driver.find_element(By.NAME, "password2").send_keys("aaa")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        erro = driver.find_element(By.CLASS_NAME, "alert-danger").text
        self.assertEqual(erro, "Usuário já existe")

        time.sleep(3)
    
    def tearDown(self):
         self.driver.quit()

if __name__ == "__main__":
    unittest.main()