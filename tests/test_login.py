import pytest
from selenium.webdriver.common.by import By
from user import usernames, password

# (Certifique-se de que a sua fixture 'browser' está definida neste ficheiro)

@pytest.mark.parametrize("usuario", usernames.values())
def test_ct001_login_sucesso(browser, usuario):
    """CT-001: Validar o acesso com credencial válida para múltiplos utilizadores"""

    print(f"Iniciando teste de login com credenciais válidas: \nUsuário: {usuario} \nSenha: {password}")

    # Em vez de um loop 'for', o pytest vai injetar a variável 'usuario' automaticamente
    browser.find_element(By.ID, "user-name").send_keys(usuario)
    browser.find_element(By.ID, "password").send_keys(password)
    browser.find_element(By.ID, "login-button").click()

    # O assert fará a validação individual para cada utilizador
    assert "inventory.html" in browser.current_url


def test_ct002_login_dados_invalidos(browser):
    """CT-002: Validar a restrição de acesso com credencial inválida"""

    print("Iniciando teste de login com credenciais inválidas: \nUsuário: usuario_falso \nSenha: senha_falsa")

    browser.find_element(By.ID, "user-name").send_keys("usuario_falso")
    browser.find_element(By.ID, "password").send_keys("senha_falsa")
    browser.find_element(By.ID, "login-button").click()

    erro = browser.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    assert "Username and password do not match" in erro

    
def test_ct003_login_campos_vazios(browser):
    """CT-003: Validar a restrição de acesso com campos vazios"""

    print("Iniciando teste de login com campos vazios")

    browser.find_element(By.ID, "login-button").click()

    erro = browser.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    assert "Username is required" in erro or "Password is required" in erro

@pytest.mark.parametrize("usuario", usernames.values())
def test_ct004_login_usuario_bloqueado(browser, usuario):
    """CT-004: Validar o acesso com utilizador bloqueado"""

    print(f"Iniciando teste de login com utilizador bloqueado: \nUsuário: {usuario} \nSenha: {password}")

    browser.find_element(By.ID, "user-name").send_keys(usuario)
    browser.find_element(By.ID, "password").send_keys(password)
    browser.find_element(By.ID, "login-button").click()

    erro = browser.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    assert "locked" in erro