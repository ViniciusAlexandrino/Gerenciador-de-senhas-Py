from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

# Função para carregar a chave de encriptação a partir de um arquivo
def load_key():
    file =  open("key.key", "rb")# Abre o arquivo 'key.key' no modo de leitura binária
    key = file.read()# Lê a chave do arquivo
    file.close()
    return key# Retorna a chave lida do arquivo

# Solicita ao usuário para inserir a senha mestra
master_pwd = input("Qual a senha? ")
key = load_key() + master_pwd.encode()# Carrega a chave e combina com a senha mestra convertida para bytes
fer = Fernet(key)# Cria um objeto Fernet para encriptação/desencriptação usando a chave combinada

# Função para visualizar as senhas salvas
def view():
    with open('senhas.txt', 'r') as f:# Abre o arquivo 'senhas.txt' no modo de leitura
        for line in f.readlines():# Lê todas as linhas do arquivo
            # Aqui dividimos a linha em 'user' e 'passw'
            user, passw = line.strip().split("|")
            print("Usuário:", user, "Senha:", fer.decrypt(passw.encode()).decode())

# Função para adicionar uma nova senha ao arquivo
def add():
    # Solicita ao usuário o nome da conta e a senha
    name = input('Nome da conta: ')
    pwd = input('Senha: ')

    with open('senhas.txt', 'a') as f:# Abre o arquivo 'senhas.txt' no modo de adição de texto
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

# Loop principal do programa para interagir com o usuário
while True:
    mode = input("Você gostaria de adicionar uma nova senha ou acessar uma existente (ver, add), ou pressione 's' para sair?").lower()
    if mode == "s": # Se o usuário quiser sair
        break
    elif mode == "ver":
        view()
    elif mode == "add":
        add()
    else:
        print("Opção inválida")
