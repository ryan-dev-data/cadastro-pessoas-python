def main():

    print("=====CADASTRO DE PESSOAS TESTE=====\n")

    quantidade = int(input("Quantas pessoas serão cadastradas: "))

    nomes = []
    idades = []

    for i in range(quantidade):

        nome = input("Digite o nome da pessoa: ")
        idade = int(input("Digite a idade da pessoa: "))
        nomes.append(nome)
        idades.append(idade)
        maiores = 0
        menores = 0

    print("\n=====CONDIÇÃO DE ENTRADA=====")
    for i in range(len(nomes)):
        if idades[i] >=18:
            print(nomes[i], "-", idades[i], "anos - Maior de idade - Acesso Liberado")
            maiores += 1
        else:
            print(nomes[i], "-", idades[i], "anos - Menor de idade - Acesso Negado")
            menores += 1

    print("\n=====CONTAGEM DE PESSOAS=====")
    print("Quantidade de pessoas :", len(nomes))
    total_pessoas = len(idades)
    media_idade = sum(idades) / total_pessoas
    maior_idade = max(idades) / total_pessoas
    menor_idade = min(idades) / total_pessoas

    #distribuição etária
    menores=0
    adultos = 0
    idosos = 0

    for idade in idades:
        if idade <18:
            menores += 1
        elif idade <60:
            adultos += 1
        else:
            idosos += 1

    #percentuais
    perc_menores = (menores/total_pessoas)*100
    perc_adultos = (adultos/total_pessoas)*100
    perc_idosos = (idosos/total_pessoas)*100

    print("\n=====ESTASTÍCAS GERAIS=====")
    print(f"Total de pessoas cadastradas: {total_pessoas}")
    print(f"Média de idade: {media_idade:.1f} anos")
    print(f"Maior de idade: {maior_idade:.1f} anos")
    print(f"Menor de idade: {menor_idade:.1f} anos")

    print("\n=====DISTRIBUIÇÃO ETÁRIA=====")
    print(f"Menores de idade: {menores} ({perc_menores:.1f}%)")
    print(f"Adultos: {adultos} ({perc_adultos:.1f}%)")
    print(f"Idosos: {idosos} ({perc_idosos:.1f}%)")

    print("\n=====ANÁLISE=====")

    if perc_adultos>50:
        print("O público é majoritariamnete adulto")
    elif perc_menores>50:
        print("O público é majoritariamente menor de idade")
    elif perc_idosos>50:
        print("O público é majoriatariamente idoso")
    else:
        print("A distribuiçâo de idades é equilibrada")

if __name__=="__main__":
    main()







