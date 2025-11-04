import string
import os
import platform
#Não mostrar passwords no terminal
from pwinput import pwinput
#Encriptar/decriptar passwords
import base64
import hashlib
from cryptography.fernet import Fernet

#Chave de encriptação simétrica
password_mestre="admin123"

def gerar_chave(master_password):
    #Gera uma chave a partir da master password.
    #Usa apenas um hash SHA-256 simples
    key = hashlib.sha256(master_password.encode()).digest()
    # Fernet requer chave base64 de 32 bytes
    return base64.urlsafe_b64encode(key)

def encrypt_password(plaintext, master_password):
    #Encripta a password em texto simples.
    #Retorna uma string base64.
    key = gerar_chave(master_password)
    fernet = Fernet(key)
    encrypted = fernet.encrypt(plaintext.encode())
    return encrypted.decode()

def decrypt_password(encrypted, master_password):
    #Desencripta a password (ou devolve None se a master password estiver errada).
    try:
        key = gerar_chave(master_password)
        fernet = Fernet(key)
        decrypted = fernet.decrypt(encrypted.encode())
        return decrypted.decode()
    except Exception:
        return None

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
    "contacto": 919384761,
    "password": encrypt_password("Password123", password_mestre)
    },
    2: {
    "nome": "Maria",
    "idade": 30,
    "cidade": "Lisboa",
    "contacto": 9283716254,
    "password": encrypt_password("Python123", password_mestre)
    },
    3: {
    "nome": "Pedro",
    "idade": 15,
    "cidade": "Coimbra",
    "contacto": 927364512,
    "password": encrypt_password("Cesae123", password_mestre)
    }
}

def mudar_password():
    global password_mestre
    password_velha = pwinput("Digite a password mestre antiga: ")
    #Pedir a password_mestre antiga ao utilizador
    if password_velha != password_mestre:
        print("Password mestre errada!")
        return
    password_mestre = pwinput("Digite a nova password mestre: ")
    for id in meu_dicionario:   #É preciso encriptar as passwords com a nova password_mestre
        meu_dicionario[id]["password"]=decrypt_password(meu_dicionario[id]["password"], password_velha)     #Desencriptar passwords com a password_mestre antiga (converter em plaintext)
        meu_dicionario[id]["password"]=encrypt_password(meu_dicionario[id]["password"], password_mestre)    #Encriptar passwords com a password_mestre nova

def listar_users(flag_informacoes=False):
    if not flag_informacoes:    #Display apenas aos nomes
        for username in meu_dicionario:
            print(f"Nome utilizador: {meu_dicionario[username]['nome']}")
    else:   #Display às informações de todos os utilizadores
        for username in meu_dicionario:
            print(f"Nome utilizador: {meu_dicionario[username]['nome']} ")
            print(f"Idade utilizador: {meu_dicionario[username]['idade']} ")
            print(f"Cidade utilizador: {meu_dicionario[username]['cidade']} ")
            print(f"Contacto: {meu_dicionario[username]['contacto']}")
            print(f"Password: {meu_dicionario[username]['password']}")
        saida=""
        while saida.lower() != "sair":
            saida=input(f"Escreva 'decrypt' para mostrar as passwords em plaintext ou 'sair' para parar de ver as informações de todos os utilizadores: ")
            if saida.lower() == "decrypt":  #Desencriptar passwords e mostrá-la
                master = input("Digite a password mestre: ").strip()
                os.system('cls') if platform.system() == "Windows" else os.system('clear')
                for username in meu_dicionario:
                    print(f"Nome utilizador: {meu_dicionario[username]['nome']} ")
                    print(f"Idade utilizador: {meu_dicionario[username]['idade']} ")
                    print(f"Cidade utilizador: {meu_dicionario[username]['cidade']} ")
                    print(f"Contacto: {meu_dicionario[username]['contacto']}")
                    plaintext=decrypt_password(meu_dicionario[username]["password"], master)    #Password plaintext
                    if plaintext is None:   #Password errada!!!
                        print(f"Password: {meu_dicionario[username]['password']}")
                        print("Para mostrar a password em plaintext digite 'decrypt'!")
                        print("Password mestre incorreta ou dados corrompidos. Não foi possível desencriptar.")
                    else:   #Password certa!!!
                        print(f"Password em plaintext: {plaintext}")

def add_user(username, age, city, contact, password):
    meu_dicionario[len(meu_dicionario)+1] = {
        "nome": username,
        "idade": age,
        "cidade": city,
        "contacto": contact,
        "password": encrypt_password(password, password_mestre) #Encriptar password
    }

#Verifica se um username já existe, True se existe
def user_exists(username):
    return any(username == id["nome"] for id in meu_dicionario.values())    #Itera por todos os registos de utilizadores e verifica o nome

def registar_utilizador():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')
    print("Bem-vindo à página de registo de utilizador")

    username = input("Username: ")
    while not username.isalnum() or user_exists(username):   #Enquanto o username não for alfanumérico ou o username não existir no sistema
        os.system('cls') if platform.system() == "Windows" else os.system('clear')
        if not username.isalnum():
            print("O username não pode ter caracteres especiais")
        else:
            print("Esse username já existe no programa!\n" \
            "Por favor introduza outro username")
        username = input("Username: ")

    os.system('cls') if platform.system() == "Windows" else os.system('clear')
    age = input("Insira a sua idade: ")
    while not age.isdigit() or int(age) < 0:    #Enquanto a idade tiver caracteres que não são dígitos [0,1,2,3,4,5,6,7,8,9] ou a idade for menor que 0
        os.system('cls') if platform.system() == "Windows" else os.system('clear')
        print("A idade tem de conter apenas números e tem de ser um número maior que 0")
        age = input("Idade: ")

    os.system('cls') if platform.system() == "Windows" else os.system('clear')
    city = input("Insira a cidade onde reside: ")
    while (any(not ch.isalpha() and not ch == " " for ch in city)) or city.lower() not in (c.lower() for c in cidades_portugal):    #Enquanto a cidade não for alfanumérica ou não pertencer à lista cidades_portugal
        os.system('cls') if platform.system() == "Windows" else os.system('clear')
        print("A cidade tem de conter apenas letras")\
            if not city.isalpha() and not any(ch == " " for ch in city) else print("Tem de ser uma cidade de Portugal. Caso contrário escrever 'Fora de Portugal'")
        city = input("Cidade: ")

    os.system('cls') if platform.system() == "Windows" else os.system('clear')
    contacto = input("Insira o contacto de telemóvel (9 números): ")
    while (len(contacto) != 9 or not contacto.startswith(tuple(["91", "92", "93", "96"]))): #Enquanto o contacto nãi tiver apenas dígitos e não tiver um prefixo válido ["91", "92", "93", "96"]
        os.system('cls') if platform.system() == "Windows" else os.system('clear')
        contacto = input("Contacto tem de conter 9 dígitos e tem de ser um número válido de Portugal: ")

    os.system('cls') if platform.system() == "Windows" else os.system('clear')
    password = pwinput()
    while (len(password)<8 or password.islower() or password.isupper() or \
           not any(ch in string.punctuation for ch in password) or \
           not any(ch.isdigit() for ch in password)):   #Segue os requisitos abaixo
        os.system('cls') if platform.system() == "Windows" else os.system('clear')
        print("Password inválida!\n" \
        "Password tem de seguir estes requisitos:\n" \
        "Tamanho mínimo: 8\n" \
        "Pelo menos 1 minúscula e 1 maiúscula\n" \
        "Pelo menos 1 número\n" \
        "Pelo menos 1 caracter especial")
        password=pwinput()

    os.system('cls') if platform.system() == "Windows" else os.system('clear')
    add_user(username, age, city.title(), contacto, password)   #Adiciona o utilizador

    print(f"O utilizador {username} for registado com sucesso!")

def editar_utilizador():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')
    sair=False
    while True:
        print("Bem-vindo à página de edição de utilizador")
        print("==========================================================================\n"
            "- Quer mostrar todos os utilizadores do sistema? (Escreva 'Sim' caso verdadeiro)\n"
            "- Escreva '0' para sair da página de edição\n"
            "==========================================================================")
        username = input("Insira o username: ")

        while True:
            if username.lower() in ['Sim','sim','s','S']:   #Mostra todos os utilizadores do sistema
                os.system('cls') if platform.system() == "Windows" else os.system('clear')
                print("Bem-vindo à página de edição de utilizador")
                print("==========================================================================\n"
                    "- Quer mostrar todos os utilizadores do sistema? (Escreva 'Sim' caso verdadeiro)\n"
                    "- Escreva '0' para sair da página de edição\n"
                    "==========================================================================")
                listar_users()  #Aqui
                username = input("Insira o username: ")
            elif username in ['0']: #Volta para o menu principal
                sair=True
                break
            elif not user_exists(username): #Se o username não existir no sistema
                os.system('cls') if platform.system() == "Windows" else os.system('clear')
                print("Bem-vindo à página de edição de utilizador")
                print("==============================================================================\n"
                "- Quer mostrar todos os utilizadores do sistema? (Escreva 'Sim' caso verdadeiro)\n"
                "- Escreva '0' para sair da página de edição\n"
                "==============================================================================")
                username = input("Username não foi encontrado no sistema\n"
                "Por favor introduza um username presente no sistema: ")
            else:   #Username presente no sistema
                break
        
        if sair: #Volta para o menu principal
            break
        
        for id,data in meu_dicionario.items():  #Encontra o id do username escolhido
            if data["nome"] == username:
                user_id = id

        print("Página de edição do utilizador "+meu_dicionario[user_id]["nome"]+
        "\n1: Editar nome\n"
        "2: Editar idade\n"
        "3: Editar cidade\n"
        "4: Editar contacto\n"
        "5: Editar password\n"
        "6: Listar informações do utilizador\n"
        "7: Remover utilizador\n"
        "0: Sair")
        
        opcao = input("O que pretende editar? ")
        
        os.system('cls') if platform.system() == "Windows" else os.system('clear')
        while True:
            while opcao not in ['1','2','3','4','5','6','7','0']:   #Enquanto a opção não for válida
                print("Página de edição do utilizador "+ meu_dicionario[user_id]["nome"] +
                "\n1: Editar nome\n"
                "2: Editar idade\n"
                "3: Editar cidade\n"
                "4: Editar contacto\n"
                "5: Editar password\n"
                "6: Listar informações do utilizador\n"
                "7: Remover utilizador\n"
                "0: Sair")
                opcao = input("Introduza uma opção válida: ")

            match(opcao):
                case "1":   #Mudar o nome
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

                case "2":   #Mudar idade
                    os.system('cls') if platform.system() == "Windows" else os.system('clear')
                    nova_idade = input("Insira nova idade: ")
                    while not nova_idade.isdigit() or int(nova_idade) < 0:
                        os.system('cls') if platform.system() == "Windows" else os.system('clear')
                        print("A idade tem de conter apenas números e tem de ser um número maior que 0")
                        nova_idade = input("Idade: ")
                    meu_dicionario[user_id]["idade"] = nova_idade
                    print("Idade atualizada com sucesso.")
                    
                case "3":   #Mudar cidade
                    os.system('cls') if platform.system() == "Windows" else os.system('clear')
                    nova_cidade = input("Insira nova cidade: ")
                    while (any(not ch.isalpha() and not ch == " " for ch in nova_cidade)) or nova_cidade.lower() not in (c.lower() for c in cidades_portugal):
                        os.system('cls') if platform.system() == "Windows" else os.system('clear')
                        print("A cidade tem de conter apenas letras")\
                            if not nova_cidade.isalpha() and not any(ch == " " for ch in nova_cidade) else print("Tem de ser uma cidade de Portugal. Caso contrário escrever 'Fora De Portugal'")
                        nova_cidade = input("Cidade: ")
                    meu_dicionario[user_id]["cidade"] = nova_cidade.title() #Capitaliza todas as palavras da string
                    print("Cidade atualizada com sucesso.")

                case "4":   #Mudar contacto
                    os.system('cls') if platform.system() == "Windows" else os.system('clear')
                    novo_contacto = input("Insira novo contacto: ")
                    while (len(novo_contacto) != 9 or not novo_contacto.startswith(tuple(["91", "92", "93", "96"]))):
                        os.system('cls') if platform.system() == "Windows" else os.system('clear')
                        novo_contacto = input("Contacto tem de conter 9 dígitos e tem de ser um número válido de Portugal: ")
                    print("Contacto atualizada com sucesso.")

                case "5":   #Mudar password
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
                    meu_dicionario[user_id]["password"] = encrypt_password(nova_password, password_mestre)
                    print("Password atualizada com sucesso.")

                case "6":   #Mostrar info de utilizador
                    os.system('cls') if platform.system() == "Windows" else os.system('clear')
                    print(f"Nome utilizador: {meu_dicionario[user_id]['nome']} ")
                    print(f"Idade utilizador: {meu_dicionario[user_id]['idade']} ")
                    print(f"Cidade utilizador: {meu_dicionario[user_id]['cidade']} ")
                    print(f"Password: {meu_dicionario[user_id]['password']}")
                    print("Para mostrar a password em plaintext digite 'decrypt'!")
                    saida = ""
                    while saida.lower() != "sair":
                        saida=input(f"Escreva 'sair' para parar de ver as informações de {meu_dicionario[user_id]['nome']}: ")
                        if saida.lower() == "decrypt":  #Mostrar password plaintext se password_mestre for a correta
                            master = input("Digite a password mestre: ").strip()
                            os.system('cls') if platform.system() == "Windows" else os.system('clear')
                            print(f"Nome utilizador: {meu_dicionario[user_id]['nome']} ")
                            print(f"Idade utilizador: {meu_dicionario[user_id]['idade']} ")
                            print(f"Cidade utilizador: {meu_dicionario[user_id]['cidade']} ")
                            plaintext=decrypt_password(meu_dicionario[user_id]["password"], master)
                            if plaintext is None:
                                print(f"Password: {meu_dicionario[user_id]['password']}")
                                print("Para mostrar a password em plaintext digite 'decrypt'!")
                                print("Master password incorreta ou dados corrompidos. Não foi possível desencriptar.")
                            else:
                                print(f"Password em plaintext: {plaintext}")

                case "7":   #Remover utilizador
                    os.system('cls') if platform.system() == "Windows" else os.system('clear')
                    while opcao.lower() not in ["sim", "nao", "s", "n"]:
                        opcao = input(f"Tem a certeza que quer remover o utilizador {meu_dicionario[user_id]['nome']} do sistema? [s/n]: ")
                    if opcao in ["sim","s"]:
                        meu_dicionario.pop(user_id)
                        break

                case "0":   #Sair
                    break
            opcao="dummy"


def menu():
    while True:
        print("==========================================\n"
        "Menu Principal\n"
        "1. Registar novo utilizador\n"
        "2. Editar utilizador\n"
        "3. Listar utilizadores no sistema\n"
        "4. Mudar password mestre\n"
        "0. Sair\n"
        "==========================================")

        opcao = input("Insira o número da opção que pretende: ")
        
        if opcao == '1':
            registar_utilizador()
        elif opcao == '2':
            editar_utilizador()
        elif opcao == '3':
            os.system('cls') if platform.system() == 'Windows' else os.system('clear')
            listar_users(True)
        elif opcao == '4':
            mudar_password()
        elif opcao == '0':
            break
        else:
            print("Opção errada! Por favor coloque uma opção válida")

    print("Obrigado por utilizar o nosso programa :D")

menu()