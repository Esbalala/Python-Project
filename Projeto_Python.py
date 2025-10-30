import string
import os
import platform
from pwinput import pwinput #Não mostrar passwords no terminal
#from time import sleep

cidades_portugal = ["Lisboa", "Porto", "Vila Nova de Gaia", "Amadora", "Braga", "Coimbra", "Funchal", "Setúbal", "Almada",
    "Aveiro", "Leiria", "Évora", "Viseu", "Faro", "Guimarães", "Barreiro", "Viana do Castelo","Torres Vedras", "Oeiras",
    "Cascais", "Matosinhos", "Maia", "Sintra", "Loures", "Ponta Delgada", "Covilhã", "Beja", "Santarém", "Tomar", "Loulé", "Fora De Portugal"
]

#Criar um dicionário de dicionários, adicionado 3 entradas dummy
meu_dicionario = {
    1: {
    "nome": "Joao",
    "idade": 25,
    "cidade": "Porto",
    "password": "Password#123"
    },
    2: {
    "nome": "Maria",
    "idade": 30,
    "cidade": "Lisboa",
    "password": "Password321*"
    },
    3: {
    "nome": "Pedro",
    "idade": 15,
    "cidade": "Coimbra",
    "password": "Cesae#123"
    }
}

def listar_users():
    for username in meu_dicionario:
        print(f"Nome utilizador: {meu_dicionario[username]['nome']}")
    #sleep(3)

def add_user(username, age, city, password):
    meu_dicionario[len(meu_dicionario)+1] = {
        "nome": username,
        "idade": age,
        "cidade": city,
        "password": password
    }

#Verifica se um username já existe, True se existe
def user_exists(username):
    return any(username == id["nome"] for id in meu_dicionario.values())    #Itera por todos os registos de utilizadores e verifica o nome

def registar_utilizador():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')
    print("Bem-vindo à página de registo de utilizador")

    username = input("Username: ")
    while not username.isalnum() or user_exists(username):   #Enquanto o username não for alfanumérico
        os.system('cls') if platform.system() == "Windows" else os.system('clear')
        if not username.isalnum():
            print("O username não pode ter caracteres especiais")
        else:
            print("Esse username já existe no programa!\n" \
            "Por favor introduza outro username")
        username = input("Username: ")

    os.system('cls') if platform.system() == "Windows" else os.system('clear')
    age = input("Insira a sua idade: ")
    while not age.isdigit() or int(age) < 0:
        os.system('cls') if platform.system() == "Windows" else os.system('clear')
        print("A idade tem de conter apenas números e tem de ser um número maior que 0")
        age = input("Idade: ")

    os.system('cls') if platform.system() == "Windows" else os.system('clear')
    city = input("Insira a cidade onde reside: ")
    while (any(not ch.isalpha() and not ch == " " for ch in city)) or city.lower() not in (c.lower() for c in cidades_portugal):
        os.system('cls') if platform.system() == "Windows" else os.system('clear')
        print("A cidade tem de conter apenas letras")\
            if not city.isalpha() and not any(ch == " " for ch in city) else print("Tem de ser uma cidade de Portugal. Caso contrário escrever 'Fora de Portugal'")
        city = input("Cidade: ")

    os.system('cls') if platform.system() == "Windows" else os.system('clear')
    password = pwinput()
    while (len(password)<8 or password.islower() or password.isupper() or \
           not any(ch in string.punctuation for ch in password) or \
           not any(ch.isdigit() for ch in password)):
        os.system('cls') if platform.system() == "Windows" else os.system('clear')
        print("Password inválida!\n" \
        "Password tem de seguir estes requisitos:\n" \
        "Tamanho mínimo: 8\n" \
        "Pelo menos 1 minúscula e 1 maiúscula\n" \
        "Pelo menos 1 número\n" \
        "Pelo menos 1 caracter especial")
        password=pwinput()

    os.system('cls') if platform.system() == "Windows" else os.system('clear')
    add_user(username, age, city.title(), password)

    print(f"O utilizador {username} for registado com sucesso!")

def editar_utilizador():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')
    sair=False
    while True:
        print("Bem-vindo à página de edição de utilizador")
        print("==========================================================================\n"
            "- Escreva 'listar_users' para mostrar todos os utilizadores do sistema\n"
            "- Escreva '0' para sair da página de edição\n"
            "==========================================================================")
        username = input("Insira o username: ")

        while True:
            if username.lower() == 'listar_users':
                os.system('cls') if platform.system() == "Windows" else os.system('clear')
                print("Bem-vindo à página de edição de utilizador")
                print("==========================================================================\n"
                    "- Escreva 'listar_users' para mostrar todos os utilizadores do sistema\n"
                    "- Escreva '0' para sair da página de edição\n"
                    "==========================================================================")
                listar_users()
                username = input("Insira o username: ")
            elif username == '0': #Volta para o menu principal
                sair=True
                break
            elif not user_exists(username):
                os.system('cls') if platform.system() == "Windows" else os.system('clear')
                print("Bem-vindo à página de edição de utilizador")
                print("==============================================================================\n"
                "- Escreva 'listar_users' para mostrar todos os utilizadores do sistema\n"
                "- Escreva '0' para sair da página de edição\n"
                "==============================================================================")
                username = input("Username não foi encontrado no sistema\n"
                "Por favor introduza um username presente no sistema: ")
            else:   #Username presente no sistema
                break
        
        if sair: #Volta para o menu principal
            break
        
        for id,data in meu_dicionario.items():
            if data["nome"] == username:
                user_id = id

        print("Página de edição do utilizador "+meu_dicionario[user_id]["nome"]+
        "\n1: Editar nome\n"
        "2: Editar idade\n"
        "3: Editar cidade\n"
        "4: Editar password\n"
        "5: Listar informações do utilizador\n"
        "6: Remover utilizador\n"
        "0: Sair")
        
        opcao = input("O que pretende editar? ")
        
        os.system('cls') if platform.system() == "Windows" else os.system('clear')
        while True:
            while opcao not in ['1','2','3','4','5','6','0']:
                print("Página de edição do utilizador "+meu_dicionario[user_id]["nome"]+
                "\n1: Editar nome\n"
                "2: Editar idade\n"
                "3: Editar cidade\n"
                "4: Editar password\n"
                "5: Listar informações do utilizador\n"
                "6: Remover utilizador\n"
                "0: Sair")
                opcao = input("Introduza uma opção válida: ")

            match(opcao):
                case "1":
                    os.system('cls') if platform.system() == "Windows" else os.system('clear')
                    novo_nome = input("Insira o novo nome: ")
                    while not novo_nome.isalnum() or user_exists(novo_nome):   #Enquanto o username não for alfanumérico
                        os.system('cls') if platform.system() == "Windows" else os.system('clear')
                        if not novo_nome.isalnum():
                            print("O username não pode ter caracteres especiais")
                        else:
                            print("Esse username já existe no programa!\n"
                            "Por favor introduza outro username")
                        novo_nome = input("Username: ")
                    meu_dicionario[user_id]["nome"] = novo_nome
                    print("Nome atualizado com sucesso.")

                case "2":
                    os.system('cls') if platform.system() == "Windows" else os.system('clear')
                    nova_idade = input("Insira nova idade: ")
                    while not nova_idade.isdigit() or int(nova_idade) < 0:
                        os.system('cls') if platform.system() == "Windows" else os.system('clear')
                        print("A idade tem de conter apenas números e tem de ser um número maior que 0")
                        nova_idade = input("Idade: ")
                    meu_dicionario[user_id]["idade"] = nova_idade
                    print("Idade atualizada com sucesso.")
                    
                case "3":
                    os.system('cls') if platform.system() == "Windows" else os.system('clear')
                    nova_cidade = input("Insira nova cidade: ")
                    while (any(not nova_cidade.isalpha() and not ch == " " for ch in nova_cidade)) or nova_cidade.lower() not in (c.lower() for c in cidades_portugal):
                        os.system('cls') if platform.system() == "Windows" else os.system('clear')
                        print("A cidade tem de conter apenas letras")\
                            if not nova_cidade.isalpha() and not any(ch == " " for ch in nova_cidade) else print("Tem de ser uma cidade de Portugal. Caso contrário escrever 'Fora De Portugal'")
                        nova_cidade = input("Cidade: ")
                    meu_dicionario[user_id]["cidade"] = nova_cidade.title() #Capitaliza todas as palavras da string
                    print("Cidade atualizada com sucesso.")

                case "4":
                    os.system('cls') if platform.system() == "Windows" else os.system('clear')
                    nova_password = pwinput("Insira nova password: ")
                    while (len(nova_password)<8 or nova_password.islower() or nova_password.isupper() or \
                    not any(ch in string.punctuation for ch in nova_password) or \
                    not any(ch.isdigit() for ch in nova_password)):
                        os.system('cls') if platform.system() == "Windows" else os.system('clear')
                        print("Password inválida!\n"
                        "Password tem de seguir estes requisitos:\n"
                        "Tamanho mínimo: 8\n"
                        "Pelo menos 1 minúscula e 1 maiúscula\n"
                        "Pelo menos 1 número\n"
                        "Pelo menos 1 caracter especial")
                        nova_password=pwinput()
                    meu_dicionario[user_id]["password"] = nova_password
                    print("Password atualizada com sucesso.")

                case "5":
                    os.system('cls') if platform.system() == "Windows" else os.system('clear')
                    print(f"Nome utilizador: {meu_dicionario[user_id]['nome']} ")
                    print(f"Idade utilizador: {meu_dicionario[user_id]['idade']} ")
                    print(f"Cidade utilizador: {meu_dicionario[user_id]['cidade']} ")
                    print(f"Password: {meu_dicionario[user_id]['password']}")
                    saida = ""
                    while saida.lower() != "sair":
                        saida=input(f"Escreva 'sair' para parar de ver as informações de {meu_dicionario[user_id]['nome']}: ")

                case "6":
                    os.system('cls') if platform.system() == "Windows" else os.system('clear')
                    while opcao.lower() not in ["sim", "nao", "s", "n"]:
                        opcao = input(f"Tem a certeza que quer remover o utilizador {meu_dicionario[user_id]['nome']} do sistema? [s/n]: ")
                    if opcao in ["sim","s"]:
                        meu_dicionario.pop(user_id)
                        break

                case "0":
                    break
            opcao="dummy"


def menu():
    while True:
        print("==========================================\n"
        "Menu Principal\n"
        "1. Registar novo utilizador\n"
        "2. Editar utilizador\n"
        "3. Listar utilizadores no sistema\n"
        "0. Sair\n"
        "==========================================")
        #4. Encriptar passwords

        opcao = input("Insira o número da opção que pretende: ")
        
        if opcao == '1':
            registar_utilizador()
        elif opcao == '2':
            editar_utilizador()
        elif opcao == '3':
            os.system('cls') if platform.system() == 'Windows' else os.system('clear')
            listar_users()
        elif opcao == '0':
            break
        else:
            print("Opção errada! Por favor coloque uma opção válida")

    print("Obrigado por utilizar o nosso programa :D")

menu()