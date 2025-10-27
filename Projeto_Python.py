#Criar uma lista com dicionários:
meu_dicionario = [{
    "nome": "Joao",
    "idade": 25,
    "cidade": "Porto"
}]
 
#Adicionar um novo dicionário á lista:
meu_dicionario.append({"nome":"Maria", "idade":30, "cidade":"Lisboa"})
print(meu_dicionario)

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



def menu():
    while True:
        print("Menu Principal")
        print("1. Registar novo utilizador")
        print("2. Editar utilizador")
        print("0. Sair")

        opcao = input("Insira o número da opção que pretende:\n")
        
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