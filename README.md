# 🧪 Trabalho-QA — Testes Automatizados

Repositório com os exercícios do trabalho da disciplina de **Qualidade e Testes de Software**. O projeto foi estruturado em **Python**, utilizando `pytest`, `selenium` e automatizado com ferramentas de tarefas do pacote `invoke`.

---

## 📂 Conteúdo Principal

- `tasks.py`: Define as tarefas automatizadas do projeto (`invoke`).
- `make_env.py`: Script focado no SO Windows para configurar e criar o ambiente rapidamente.
- `conftest.py`: Configurações globais e *fixtures* base do `pytest` (ex.: `browser`).
- `tests/`: Suítes de testes automatizados separados por contexto funcional (`login`, `inventory`, `cart`, `checkout`).
- `requirements.txt`: Relação de pacotes e dependências de execução.

---

## 🚀 Pré-requisitos

- **Python** (versão 3.8 ou superior).
- **Google Chrome** instalado.
- **Chromedriver** compatível com a versão instalada adicionado no PATH (ou via library *webdriver-manager*).

---

## ⚙️ Instalação e Setup

### 🪟 Instalação Rápida para Windows (Powershell)

O projeto conta com o script `make_env.py`, que encarrega-se de criar o diretório virtual (`.venv`), liberar escopo de execução remote-signed para a sessão atual e instalar os pacotes essenciais para tarefas (`invoke`) e base (pip).

```powershell
python make_env.py
```

*Lembre-se de ativar o ambiente logo após executá-lo:*
```powershell
.\.venv\Scripts\Activate.ps1
```

<details>
<summary><b>🛠 Instalação Manual (Outros Sistemas Operacionais)</b></summary>

1. Criar e ativar o ambiente virtual:
```bash
python -m venv .venv
# Mac/Linux: source .venv/bin/activate
```
2. Instalar a biblioteca de ferramentas de task:
```bash
pip install invoke
```
</details>

### Baixando as Requisições do Projeto
Com o ambiente ativado e o pacote Invoke preparado, obtenha as dependências executando:
```bash
invoke install
```
*(Funciona como o tradicional `pip install -r requirements.txt`)*

---

## 🛠️ Comandos `invoke` (Tasks)

As tarefas criadas no arquivo `tasks.py` eliminam o excesso de comandos longos facilitando os gatilhos:

| Comando Invoke | Descrição |
|---|---|
| `invoke install` | Instala todas as dependências requeridas utilizando o pip. |
| `invoke test` | Varre a pasta de testes e executa **todas** as baterias do pytest juntas. |
| `invoke test --test-name=<suite>` | Executa uma suíte filtrada. Valores aceitos: `login`, `inventory`, `cart` ou `checkout`. |
| `invoke test --test-name=<suite> --test-func=<função>` | Executa apenas o de cenário teste alvo passando a assinatura (via *nodeid `::`*). |
| `invoke zip-windows` | Varre e encapsula o projeto atual num arquivo `.zip` seguro (excluindo os diretórios ocultos e grandes como `.venv` e `__pycache__`). |
| `invoke zip-windows --name "meu-trabalho.zip"`| Compacta o projeto aplicando o nome de escolha que for provido. |

**Exemplo Prático (Apenas Teste de Login - Caso de Teste 001)**:
```bash
invoke test --test-name login --test-func test_ct001
```

---

## 🧪 Comandos Diretamente com `pytest`

Caso você não queira utilizar o `invoke` em algum cenário específico e preferir os gatilhos brutos do `pytest`:

```bash
# Rodar toda a suite
python -m pytest -q

# Rodar todos de uma classe especifica
python -m pytest tests/test_login.py -v

# Selecionar filtrando pelas expressões nomeadas de funções 
python -m pytest -k "login and test_ct001"
```

---

## 🌐 Sobre o WebDriver (Selenium)

Este projeto encapsula e automatiza toda instanciação do `webdriver` dentro da *fixture* `browser` declarada em `conftest.py`. O WebDriver inicializa a conexão e realiza o *teardown* ao final injetando estabilidade nos relatórios e não necessitando invocações explícitas manuais por função.

---

## ⚠️ Problemas Comuns

- **`ModuleNotFoundError: No module named 'invoke'`**: O utilitário foi perdido do ambiente / O ambiente virtual parou de ser reconhecido; rode o seu comando de `Activate.ps1`.
- **PowerShell reclamando de Scripts Seguros (Bloqueado)**: Digite para o modo atual `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`.

Arquivos importantes
- [tasks.py](tasks.py)
- [conftest.py](conftest.py)
- [browser.py](browser.py)
- [tests/test_login.py](tests/test_login.py)
- [requirements.txt](requirements.txt)

