# Função principal
def verificar_idade():
    # Solicita a idade do usuário
    idade = input("Digite a sua idade: ")

    # Verifica se a entrada é um número
    if not idade.isdigit():
        print("Por favor, digite um número válido para a idade.")
        return

    # Converte a idade para um número inteiro
    idade = int(idade)

    # Verifica se a idade é válida (entre 0 e 120 anos)
    if idade < 0 or idade > 120:
        print("A idade digitada não é válida. A idade deve ser entre 0 e 120 anos.")
    else:
        # Verifica se a pessoa é maior ou menor de idade
        if idade >= 18:
            print("Você é maior de idade.")
        else:
            print("Você é menor de idade.")

# Chama a função
verificar_idade()
