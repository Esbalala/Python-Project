import string

#Criar uma lista com dicionários:
meu_dicionario = {
    1 : {"nome": "Ana", "idade": 28, "cidade": "Porto", "password": "abc"},
    2 : {"nome": "Joao", "idade": 35, "cidade": "Lisboa", "password": "123"},
    3 : {"nome": "Marta", "idade": 22, "cidade": "Coimbra", "password": "xyz"}
}

print(meu_dicionario[1]["nome"])
 


print(meu_dicionario)
print(meu_dicionario[1]["idade"])

#Verifica se um username já existe, True se existe
def user_exists(user):
    return True if user in meu_dicionario else False

def registar_utilizador():
    print("Bem-vindo à página de registo de utilizador")

    username = input("Username: ")
    while not username.isalnum() or user_exists(username):   #Enquanto o username não for alfanumérico
        if not username.isalnum():
            print("O username não pode ter caracteres especiais")
        else:
            print("Esse username já existe no programa!\n" \
            "Por favor introduza outro username")

        username = input("Username: ")

    password = input("Password: ") #COLOCAR LIMITACOES!!!
    while (len(password)<8 or password.islower() or password.isupper() or all(ch in string.punctuation for ch in password) or \
           all(ch in string.digits for ch in password)):
        input("Password inválida!" \
        "Password tem de seguir estes requisitos:" \
        "Tamanho mínimo: 8" \
        "Pelo menos 1 minúscula e 1 maiúscula" \
        "Pelo menos 1 número" \
        "Pelo menos 1 caracter especial")

def editar_utilizador():
    username = input(f"Insira o username:")

    print(f"1: Editar nome")
    print(f"2: Editar idade")
    print(f"3: Editar cidade")
    print(f"4: Editar password")
    print(f"5: Listar utilizador")
    
    opcao = input(f"O que pretende editar? \n")
    

    for id,data in meu_dicionario.items():
        
        if data["nome"] == username:
            user_id = id

    match(opcao):
        case "1":
            novo_nome = input(f"Insira o novo nome: ")
            meu_dicionario[user_id]["nome"] = novo_nome
            print("Nome atualizado com sucesso.")
        case "2":
            nova_idade = input(f"Insira nova idade: ")
            meu_dicionario[user_id]["idade"] = nova_idade
            print("Idade atualizada com sucesso.")
        case "3":
            nova_cidade = input(f"Insira nova idade: ")
            meu_dicionario[user_id]["cidade"] = nova_cidade
            print("Cidade atualizada com sucesso.")
        case "4":
            nova_password = input(f"Insira nova password: ")
            meu_dicionario[user_id]["password"] = nova_password
            print("Password atualizada com sucesso.")
        case "5":
            print(f"Nome utilizador: {meu_dicionario[user_id]["nome"]} ")
            print(f"Idade utilizador: {meu_dicionario[user_id]["idade"]} ")
            print(f"Cidade utilizador: {meu_dicionario[user_id]["cidade"]} ")
   
def listar_users():
        for username in meu_dicionario:
            print(f"Nome utilizador: {meu_dicionario[username]["nome"]} \n")

def menu():
    while True:
        print("Menu Principal")
        print("1. Registar novo utilizador")
        print("2. Editar utilizador")
        print("3. Listar Utilizadores")
        print("0. Sair")

        opcao = input("Insira o número da opção que pretende:\n")
        
        if opcao == '1':
            registar_utilizador()
        elif opcao == '2':
            editar_utilizador()
        elif opcao == '3':
            listar_users()
        elif opcao == '0':
            break
        else:
            print("Opção errada! Por favor coloque uma opção válida")

    print("Obrigado por utilizar o nosso programa :D")




menu()