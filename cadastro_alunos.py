# Função que classifica o aluno de acordo com a nota
def classificar(notas):
    if notas >= 7:
        return "aprovado"
    elif notas >= 5:
        return "recuperação"
    else:
        return "reprovado"

# Função que calcula a média das notas da turma
def media_alunos(alunos):
    notas = [aluno["notas"] for aluno in alunos]  # pega todas as notas
    return sum(notas) / len(notas)  # soma e divide pelo total de alunos

# Lista que vai armazenar os alunos cadastrados
alunos = []

# Loop principal de cadastro
while True:
    # Cadastro do nome
    while True:
        nome = input("Digite o nome do aluno: ")#pede o nome para o usuario
        if nome.strip() == "":  # impede de entrar espaços vazios
            print("Nome não pode ficar vazio")
        elif not nome.replace(" ", "").isalpha():  # impede números e símbolos
            print("Digite apenas letras (sem números ou símbolos)")
        else:
            break
    # Cadastro da idade
    while True:
    #try/except evita que o site quebre
        try:
            idade = int(input("Digite a idade do aluno: "))#pede a idade com numero int
            if idade <= 0:  # idade inválida
                print("Idade inválida, tente novamente")
            else:
                break
        except:
            print("Você digitou algo errado!")

    # Cadastro da nota
    while True:
        try:
            notas = float(input("Digite a nota do aluno: "))#pede um numero de 0-10
            if notas < 0 or notas > 10:  #nota fora do intervalo
                print("Nota inválida, digite a nota de 0-10")
            else:
                break
        except:
            print("Você digitou uma nota inválida!")

    #Cria o dicionário do aluno
    aluno = {
        "nome": nome,
        "idade": idade,
        "notas": notas,
        "situacao": classificar(notas)
    }

    # Adiciona o aluno na ultima posicao da lista
    alunos.append(aluno)

    # Pergunta se deseja continuar cadastrando
    while True:
        continuar = input("Deseja cadastrar outro aluno? (s/n): ").strip().lower()
        if continuar == "s":
            break  # volta para cadastrar outro aluno
        elif continuar == "n":
            break  # sai do mini loop
        else:
            print("Digite apenas s ou n.")

    # Se o usuário digitou "n", encerra o loop principal
    if continuar == "n":
        break

# Exibe lista de alunos cadastrados
print("\n === Lista de alunos ===\n")
for aluno in alunos:
    print(f"Nome: {aluno['nome']}")
    print(f"Idade: {aluno['idade']}")
    print(f"Notas: {aluno['notas']}")
    print(f"Situação: {aluno['situacao']}")
    print("-" * 25)

# Exibe média da turma
print("\n === Média final da turma ===\n")
print(media_alunos(alunos))

# Relatório final de aprovados, recuperação e reprovados
print("\n === Relatório final ===\n")
aprovado = 0
recuperacao = 0
reprovado = 0

for aluno in alunos:
    resultado = classificar(aluno["notas"])
    if resultado == "aprovado":
        aprovado += 1
    elif resultado == "recuperação":
        recuperacao += 1
    else:
        reprovado += 1

print("Aprovados: ", aprovado)
print("Em recuperação: ", recuperacao)
print("Reprovados: ", reprovado)

# Descobre maior e menor nota
maior_nota = alunos[0]
menor_nota = alunos[0]

for aluno in alunos:
    if aluno["notas"] > maior_nota["notas"]:
        maior_nota = aluno
    if aluno["notas"] < menor_nota["notas"]:
        menor_nota = aluno

print("\nMaior nota: ", maior_nota["nome"], "=", maior_nota["notas"])
print("Menor nota: ", menor_nota["nome"], "=", menor_nota["notas"])
