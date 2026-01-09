# 1. Criar matriz com 5 chamados
chamados = [
    ["001", "Alice",  "Erro no login",              "Aberto"],
    ["002", "Bruno",  "Problema na impressora",     "Em andamento"],
    ["003", "Carmen", "Computador não liga",        "Fechado"],
    ["004", "Diego",  "Tela azul ao iniciar",       "Aberto"],
    ["005", "Emily",  "Sistema muito lento",        "Em andamento"]
]

# 2. Imprimir todos os chamados
print("===== TODOS OS CHAMADOS =====")
for chamado in chamados:
    print(chamado)

# 3. Exibir apenas chamados com status "Aberto"
print("\n===== CHAMADOS ABERTOS =====")
for chamado in chamados:
    if chamado[3] == "Aberto":
        print(chamado)

# 4. Alterar status de um chamado "Aberto" para "Fechado"
# Vamos fechar o chamado de ID "004", por exemplo
for chamado in chamados:
    if chamado[0] == "004":
        chamado[3] = "Fechado"

print("\n===== MATRIZ ATUALIZADA =====")
for chamado in chamados:
    print(chamado)

# 5. (Opcional) Função para buscar um chamado pelo ID
def buscar_chamado(lista, id_procurado):
    for chamado in lista:
        if chamado[0] == id_procurado:
            return chamado
    return "Chamado não encontrado."

# Teste da função (opcional):
print("\n===== BUSCA POR CHAMADO =====")
print(buscar_chamado(chamados, "002"))
