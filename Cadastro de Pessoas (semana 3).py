print("=====CADASTRO DE PESSOAS=====")

quantidade = int(input("Quantas pessoas serão cadastradas? "))

nomes = []
idades = []

for i in range(quantidade):
    nome = str(input("Digite o nome: "))
    idade = int(input("Digite a idade: "))

    nomes.append(nome)
    idades.append(idade)

maiores = 0
menores = 0

print("=====CONDIÇÕES DE ENTRADA=====\n")
for i in range(len(nomes)):
     if idades[i]>=18:
        print(nomes[i], "-", idades[i], "anos - Acesso liberado")
        maiores += 1
     else:
        print(nomes[i], "-", idades[i], "anos - Acesso negado")
        menores += 1

print("\n=====CONTAGEM DE PESSOAS=====")
print("Total de pessoas: ", len(nomes))
print("Maiores de idade: ", maiores)
print("Menores de idade: ", menores)




