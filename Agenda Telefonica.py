# Lista que armazenará os contatos
contatos = []

# Função para adicionar contato
def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    contatos.append({"nome": nome, "telefone": telefone})
    print("Contato adicionado com sucesso!\n")

# Função para listar contatos
def listar_contatos():
    if not contatos:
        print("Nenhum contato cadastrado.\n")
        return

    print("\nLista de contatos:")
    for i, contato in enumerate(contatos):
        print(f"{i} - Nome: {contato['nome']} | Telefone: {contato['telefone']}")
    print()

# Função para atualizar contato
def atualizar_contato():
    listar_contatos()
    if not contatos:
        return

    try:
        indice = int(input("Digite o índice do contato que deseja atualizar: "))
        if indice < 0 or indice >= len(contatos):
            print("Índice inválido.\n")
            return

        novo_nome = input("Digite o novo nome (ou pressione Enter para manter): ")
        novo_telefone = input("Digite o novo telefone (ou pressione Enter para manter): ")

        if novo_nome:
            contatos[indice]["nome"] = novo_nome
        if novo_telefone:
            contatos[indice]["telefone"] = novo_telefone

        print("Contato atualizado com sucesso!\n")
    except ValueError:
        print("Entrada inválida.\n")

# Função para excluir contato
def excluir_contato():
    listar_contatos()
    if not contatos:
        return

    try:
        indice = int(input("Digite o índice do contato que deseja excluir: "))
        if indice < 0 or indice >= len(contatos):
            print("Índice inválido.\n")
            return

        contatos.pop(indice)
        print("Contato excluído com sucesso!\n")
    except ValueError:
        print("Entrada inválida.\n")

# Função principal (menu)
def menu():
    while True:
        print("=== Agenda Telefônica ===")
        print("1 - Adicionar contato")
        print("2 - Listar contatos")
        print("3 - Atualizar contato")
        print("4 - Excluir contato")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_contato()
        elif opcao == "2":
            listar_contatos()
        elif opcao == "3":
            atualizar_contato()
        elif opcao == "4":
            excluir_contato()
        elif opcao == "5":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Execução do programa
menu()

