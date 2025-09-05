perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opcoes': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opcoes': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opcoes': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0 

for pergunta in perguntas:
    print("\n" + pergunta["Pergunta"])
    for i, opcao in enumerate(pergunta['Opcoes']):
        print(f"{i}) {opcao}")
    
    
    indice_digitado = int(input("Digite o número da resposta: "))
    
    
    opcao_escolhida = pergunta['Opcoes'][indice_digitado]

    if opcao_escolhida == pergunta["Resposta"]:
        print("Acertou ")
        acertos += 1
    else:
        print(f"Errou . A resposta certa é: {pergunta['Resposta']}")

print(f"\nVocê acertou {acertos}/{len(perguntas)} perguntas")
