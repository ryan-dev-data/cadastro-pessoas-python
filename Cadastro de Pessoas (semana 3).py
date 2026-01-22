print("=====CADASTRO DE PESSOAS=====\n")

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
        print(nomes[i], "-", idades[i], "anos - Maior de idade")
        maiores += 1
    else:
        print(nomes[i], "-", idades[i], "anos - Menor de idade")
        menores += 1



print("\n=====CONTAGEM DE PESSOAS=====")
print("Quantidade de pessoas :", len(nomes))
total = len(nomes)
perc_maiores = (maiores/total)*100
perc_menores = (menores/total)*100
print(f"Maiores de idade:  {maiores} ({perc_maiores:.1f}%)")
print(f"Menores de idade:  {menores} ({perc_menores:.1f}%)")

print("\n=====PÚBLICO MAJORITÁRIO=====")
if perc_maiores>50:
    print("\nPublico majoriatariamente maior de idade")
else:
    print("\nPublico majoriatariamente menor de idade")





