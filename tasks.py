from invoke import task
from datetime import datetime
import os
import zipfile


@task
def install(c):
    c.run("pip install -r requirements.txt")

@task
def test(c, test_name=None, test_func=None):

    test_dir = "tests"

    if test_name:

        if test_name == "login":
            test_dir = test_dir + "/test_login.py"

        elif test_name == "inventory":
            test_dir = test_dir + "/test_inventory.py"

        elif test_name == "cart":
            test_dir = test_dir + "/test_cart.py"

        elif test_name == "checkout":
            test_dir = test_dir + "/test_checkout.py"

        else:            
            print("NOME INVÁLIDO \nTESTES DISPONÍVEIS: login, inventory, cart, checkout.")
            return

        if test_func:            
            test_dir = test_dir + f"::{test_func}"

        test_dir.strip().lower()
        c.run(f"pytest {test_dir} -v")

    else:
        test_dir = test_dir + "/"
        c.run(f"pytest {test_dir} -v")

@task
def zip_windows(c, name=None):

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    zip_filename = name or f"Trabalho-QA-{timestamp}.zip"
    zip_path = os.path.abspath(os.path.join("..", zip_filename))

    print(f"→ Criando ZIP: {zip_path}")

    excludes = [
        "venv",
        "__pycache__",
        ".git",
        ".vscode",
        "delivery.egg-info"
    ]

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk("."):

            dirs[:] = [d for d in dirs if d not in excludes]

            for file in files:
                if file.endswith((".pyc", ".pyo", ".pyd", ".log", ".db", ".sqlite3")):
                    continue

                filepath = os.path.join(root, file)
                zipf.write(filepath)

    if os.path.exists(zip_path):
        size_mb = os.path.getsize(zip_path) / (1024 * 1024)
        print(f"→ ZIP criado com sucesso: {zip_path}")
        print(f"   Tamanho: {size_mb:.2f} MB")