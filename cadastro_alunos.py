#essa função classifica se o aluno foi aprovado, reprovado ou se ele está de recuperação.
def classificar(notas):
  if notas >= 7:
    return("aprovado")
  elif notas >= 5:
    return("recuperação")
  else: 
    return("reprovado")
#essa função faz a média dos alunos cadastrados.
def media_alunos(alunos):
   notas = [aluno["notas"]for aluno in alunos]
   return sum(notas) / len(notas)
#lista alunos.
alunos = []
#while true deixa tudo verdadeiro para rodar o break
while True:
 while True:
#pede o nome para o usuário
  nome = input("digite o nome do aluno:")
  #strip apaga os espaços em branco e se estiver vazio, pede para que o usuario digite novamente seu nome
  if nome.strip() =="":
    print("Nome não pode ficar vazio")
#isalpha aceita somente letras(A-Z),.replace(" ","") permite espaço, not entra no erro se tiver algo errado
  elif not nome.replace(" ","").isalpha():
    print("Digite apenas letras(sem números ou símbolos)")
  else:
    break
#while cria o loop e o true deixa sempre verdadeiro 
 while True: 
#try tenta executar e se nao der certo vai pro except até o usuário digitar uma idade válida.
    try:
#variavel idade atrelada ao input q esta configurado para receber apenar numeros inteiros e o input esta printando para o usuário digitar a idade do próprio.
        idade = int(input("digite a idade do aluno:"))
#se idade for menor ou igual a zero, o console printa invalido.
        if idade <= 0:
           print("idade inválida, tente novamente")
# se a idade for maior que 0, o loop é encerrado
        else:
           break
      #se chegou aqui ele vai printar que deu erro e vai começar o loop dnv ate o usuario digitar corretamente,
    except:
        print("você digitou algo errado!")
#while cria um loop e true deixa sempre verdadeiro
 while True:
#try tenta executar e se n der certo vai pro except até o usuário digitar um nota válida.
    try: 
#notas aceitando apenas numeros entre 0-10
        notas = float(input("digite a nota do aluno:"))
# se a nota for menor que 0 ou maior que 10, mostra mensagem de erro e pede novamente
        if notas < 0 or notas > 10:
          print("nota inválida, digite a nota de 0-10")
#se n vida que segue
        else:
            break
#se entrar no except vai printar invalido e comecar o loop dnv
    except:
        print("você digitou uma nota inválida!")
#dicionario "aluno" 
 aluno = {
 "nome": nome,
 "idade": idade,
 "notas": notas,
 "situacao": classificar(notas)
 }
sair = False # variável começa falsa, usada para controlar encerramento do cadastro
alunos.append(aluno)  # adiciona dicionário dentro da lista alunos

while True:# inicia laço para validar a resposta do usuário
        continuar = input("Deseja cadastrar outro aluno? (s/n): ").strip().lower()# pede resposta, remove espaços e converte para minúsculo

        if continuar in ["s", "sim"]:# verifica se usuário deseja continuar cadastrando
            break  # sai do laço da resposta

        elif continuar in ["n", "nao", "não"]: # verifica se usuário deseja encerrar cadastro
            sair = True # altera variável para indicar saída do programa
            break # sai do laço da pergunta

        else: # caso digite algo diferente das opções válidas
            print("Digite apenas S/N, Sim ou Não.")# exibe mensagem de erro

        if sair: # verifica se usuário escolheu encerrar
         break # encerra o laço principal do cadastro

#cabecalho
print("\n ===Lista de alunos===\n")
#for percorrendo dict aluno dentro da list alunos, bem intuitivo.
for aluno in alunos:
   print(f"nome: {aluno['nome']}")
   print(f"idade: {aluno['idade']}")
   print(f"notas: {aluno['notas']}")
   print(f"situação: {aluno['situacao']}")
   print("\n")
   print("-" * 25)
#cabecalho
print("\n ===Média final da turma===\n")
#mostra a media dos alunos, puxando a funçao da L10
print (media_alunos(alunos))
#cabecalho
print("\n ===Relatório final===\n")
#contadores para cada situação
aprovado = 0
recuperacao = 0 
reprovado = 0
#percorre a lista de alunos e classifica cada um
for aluno in alunos:
  resultado = classificar(aluno["notas"])
#add ao contador de acordo com a situação retornada
  if resultado == "aprovado":
    aprovado += 1
  elif resultado == "recuperação":
    recuperacao += 1
  else:
    reprovado += 1
#mostra o resultado final
print("aprovado: ", aprovado)
print("Em recuperação: ", recuperacao)
print("reprovados: ", reprovado)
#usei para pular uma linha 
print("\n")
#pega o primeiro aluno da lista como referencia da menor e maior nota
maior_nota = alunos[0]
menor_nota = alunos[0]
#percorre todos os alunos da lista
for aluno in alunos:
   if aluno["notas"] > maior_nota["notas"]:
      maior_nota = aluno #atualiza o aluno com maior nota
   if aluno["notas"] < menor_nota["notas"]:
      menor_nota = aluno #atualiza o aluno com menor nota
#mostra o aluno com maior nota
print("Maior nota: ",maior_nota["nome"], "=", maior_nota["notas"])
#mostra o aluno com menor nota
print("Menor nota: ",menor_nota["nome"], "=", menor_nota["notas"])
