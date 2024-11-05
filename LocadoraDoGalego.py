opcao = 1
filmes = []

print("===== LOCADORA DO GALEGO =====")

while opcao != 5:
    print("""
    1) Listar filmes
    2) Adicionar filme
    3) Pesquisar filme pelo código
    4) Remover filme pelo código
    5) Sair
    """)
    
    opcao = int(input(" -> Digite sua opção [1-5]: "))
    print()
    
    if opcao == 1:
        if len(filmes) > 0:
            print("===== LISTA DE FILMES =====")
            print()
            for i in range(len(filmes)):  # Gera uma lista com o tamanho da lista de filmes
                print(f"{i + 1} - {filmes[i]}")  # Exibe o índice +1 e o nome do filme correspondente na lista
        else:
            print("[ERRO] Não existem filmes cadastrados!")
    
    elif opcao == 2:
        novoFilme = input("Digite o nome do filme que deseja cadastrar: ")
        filmes.append(novoFilme) 
        print(f"'{novoFilme}' foi cadastrado com sucesso!")
    
    elif opcao == 3:
        codigo = int(input("Digite o código do filme que deseja pesquisar: "))
        print()
        if 1 <= codigo <= len(filmes):  # Verifica se o código está dentro do intervalo válido
            print(f"Código: {codigo} \nFilme: {filmes[codigo - 1]}")
        else:
            print("[ERRO] Código inválido!")

    elif opcao == 4:
        if len(filmes) == 0:
            print("[ERRO] Não há nenhum filme para remover!")
        else:
            remover = int(input("Digite o código do filme que deseja remover: "))
            if 1 <= remover <= len(filmes):  
                filme_removido = filmes.pop(remover - 1)  # Remove o filme e armazena o nome dele
                print(f"O filme '{filme_removido}' foi removido com sucesso!") 
            else:
                print("[ERRO] Código inválido!")
    
    elif opcao != 5:
        print("[ERRO] Opção Inválida, tente novamente.")
        
print("Obrigado por usar nossa locadora, até mais!")
