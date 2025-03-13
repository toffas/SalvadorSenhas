import random
import json

def gerar_senha():
    password = ""
    caracters = "AabBCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890!@#$%&*"
    for digito in range(12): 
        aleatorio = random.choice(caracters)
        password += aleatorio
    return password

try:
    with open("login.json", "r", encoding="utf-8") as arquivo:
        dados_existentes = json.load(arquivo)
       
        if not isinstance(dados_existentes, list):
            dados_existentes = []
except FileNotFoundError:
    dados_existentes = []


login = input("Login: ")

login_existente = False
for usuario in dados_existentes:
    if usuario["login"] == login:
        
        login_existente = True
        usuario["password"] = gerar_senha()
        print(f"A senha para o login '{login}' foi atualizada.")
        break


if not login_existente:
    
    password = gerar_senha()
    dados_existentes.append({
        "login": login,
        "password": password
    })
    print(f"Novo login e senha para '{login}' foram adicionados.")

with open("login.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados_existentes, arquivo, ensure_ascii=False, indent=4)

print("Login e senha salvos no arquivo 'login.json'.")
