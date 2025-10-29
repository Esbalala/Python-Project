import string
import os   #Para limpar terminal
import platform

cidades_portugal = ["Lisboa", "Porto", "Vila Nova de Gaia", "Amadora", "Braga", "Coimbra", "Funchal", "Setúbal", "Almada",
    "Aveiro", "Leiria", "Évora", "Viseu", "Faro", "Guimarães", "Barreiro", "Viana do Castelo","Torres Vedras", "Oeiras",
    "Cascais", "Matosinhos", "Maia", "Sintra", "Loures", "Ponta Delgada", "Covilhã", "Beja", "Santarém", "Tomar", "Loulé", "Fora de Portugal"
]
#Criar uma lista com dicionários:
meu_dicionario = {
    1: {
    "nome": "Joao",
    "idade": 25,
    "cidade": "Porto",
    "password": "password123"
    }
}

def asd(city_name):
    #for cidade in cidades_portugal:
    #    print(cidade)

    if city_name.lower() not in (c.lower() for c in cidades_portugal):
        print("NAO")  # Not found
    else:
        print("SIM")  # Found

asd("Porto")
 
#Adicionar uma entrada ao dicionário:
meu_dicionario[2] = {
    "nome": "Maria",
    "idade": 30,
    "cidade": "Lisboa",
    "password": "password123"
}

def add_user(username, age, city, password):
    meu_dicionario[len(meu_dicionario)+1] = {
        "nome": username,
        "idade": age,
        "cidade": city.capitalize(),
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
        age = input("A idade tem de ser um número maior que 0:\n" \
        "Idade: ")
    
    os.system('cls') if platform.system() == "Windows" else os.system('clear')
    city = input("Insira a sua cidade: ")
    while (any(not ch.isalpha() and not ch == " " for ch in city)) or city.lower() not in (c.lower() for c in cidades_portugal):
        os.system('cls') if platform.system() == "Windows" else os.system('clear')
        print("A cidade tem de conter apenas letras")\
            if not city.isalpha() and not any(ch == " " for ch in city) else print("Tem de ser uma cidade de Portugal. Caso contrário escrever 'Fora de Portugal'")
        city = input("Cidade: ")

    os.system('cls') if platform.system() == "Windows" else os.system('clear')
    password = input("Password: ")
    while (len(password)<8 or password.islower() or password.isupper() or \
           not any(ch in string.punctuation for ch in password) or \
           not any(ch.isdigit() for ch in password)):
        os.system('cls') if platform.system() == "Windows" else os.system('clear')
        password=input("Password inválida!\n" \
        "Password tem de seguir estes requisitos:\n" \
        "Tamanho mínimo: 8\n" \
        "Pelo menos 1 minúscula e 1 maiúscula\n" \
        "Pelo menos 1 número\n" \
        "Pelo menos 1 caracter especial\n" \
        "Password: ")
    print("Password válida!")

    os.system('cls') if platform.system() == "Windows" else os.system('clear')
    add_user(username, age, city, password)

    print(f"O utilizador {username} for registado com sucesso!")


def menu():
    while True:
        print("==========================================")
        print("Menu Principal")
        print("1. Registar novo utilizador")
        print("2. Editar utilizador")
        print("0. Sair")
        print("==========================================")

        opcao = input("Insira o número da opção que pretende: ")
        
        if opcao == '1':
            registar_utilizador()
        elif opcao == '2':
            editar_utilizador()
        elif opcao == '0':
            break
        else:
            print("Opção errada! Por favor coloque uma opção válida")

    print("Obrigado por utilizar o nosso programa :D")

menu()