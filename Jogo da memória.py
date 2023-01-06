#importações
import time
import random
import os

#Declaração de variaveis e listas
numeros = []
x = 0
y = 0
sair = 0
JogarDenovo = "S"
contador = 4
vitoria = 0
derrota = 0
numero = 0


#cadastro
def cadastro():
  nome = input("Digite seu nome: ")
  print(f'Bem-Vindo {nome}!')
  time.sleep(3)
  os.system("clear")
  print(f'Bem-Vindo {nome}!')


#regras
def regras():
  global sair
  esc = input("Deseja ver as regras? digite (s)sim ou (n)não: ")
  esc = esc.upper()

  if esc == "S":
    sair = 1
  elif esc == "N":
    sair = 1

  #Filtro para a entrada inválida
  while sair == 0:
    esc = input("Valor Inválido digite apenas (s) sim ou (n) não: ")
    esc = esc.upper()
    if esc == "S":
      sair = 1
    if esc == "N":
      sair = 1

  #Mostrar as regras
  if esc == "S":
    print("Serão colocados 5 números sorteados aleatoriamente de 1-50.")
    time.sleep(4)
    print("Você terá que decorar em 5 segundos.")
    time.sleep(3)
    print("Após os 5 segundos a tela será apagada, e você devera listar os 5 números em ordem")
    print()
    print("redirecionando...")
    time.sleep(4)
    os.system("clear")
    
  #Saída direto pro jogo (menos bruta)
  elif esc == "N":
    print("Ok")
    print()
    print("redirecionando...")
    time.sleep(4)
    os.system("clear")


#Sortear os numeros (Esse deu trabalho kk)
def sortearNumero():
  global numeros
  global x

  numero_sorteado = random.randint(1, 50)
  i = 0
  igual = False
  while i != x:
    if numero_sorteado == numeros[i]:
      igual = True
      sortearNumero()
    i += 1
  if igual == False:
    numeros.append(numero_sorteado)
    x += 1


rep = 0

#Laço que irá sortear os numeros
while rep != 5:
  sortearNumero()
  rep += 1


#Função para o usuário continuar jogando (Outro que deu trabalho kk)
def JogarNovamente():
  #Declaração de variáveis globais
  global JogarDenovo
  global y
  global numeros
  global x

  #Escolha do jogador para a proxima partida
  time.sleep(2)
  JogarDenovo = input("Deseja jogar denovo? (s/n): ")
  JogarDenovo = JogarDenovo.upper()
  
  #Saída para a próxima partida
  if JogarDenovo == "S":
    y = 1
    x = 0
    numeros = []
    rep = 0
    while rep != 5:
      sortearNumero()
      rep += 1

  #Fim do jogo(escolha)
  elif JogarDenovo == "N":
    y = 1

  #Filtro de entrada inválida de dados
  while y == 0:
    JogarDenovo = input("Valor inválido digite (s)sim ou (n)não: ")
    JogarDenovo = JogarDenovo.upper()
    if JogarDenovo == "S":
      y = 1
      x = 0
      numeros = []
      rep = 0
      while rep != 5:
       sortearNumero()
       rep += 1
      
    elif JogarDenovo == "N":
      y = 1

  os.system("clear")

#Função para filtrar a entrada de caracteres inválidas nos ifs finais 
def numeros_invalidos():
  global numero
  while numero.isnumeric() == False:
    print("Somente numeros positivos são aceitos letras ou caracteres não")
    numero = input("Adivinhe o número: ")
  numero = int(numero)

#Função para impedir que o jogador coloque um nuero maior que 50
def limite():
  global numero
  limite = 50
  while numero > limite or numero <= 0:
      print("Não passe do limite de 1 a",limite)
      numero=int(input("Digite novamente: "))
    
#Função do Jogo
def jogo():
  #declaração de variáveis globais
  global contador
  global vitoria
  global derrota
  global numero

  #Laço de repetição com ligação a futura escolha do jogador
  while JogarDenovo == "S":
    print("Vamos começar o jogo!")
    #contagem regressiva
    while contador > 1:
      time.sleep(1)
      contador -= 1
      print(contador)

  #Mostrar números para o usuário
    time.sleep(1)
    print(numeros)
    time.sleep(5)
    os.system("clear")

    #Pedir para o usuário digitar os numeros
    numero = input("Digite o primeiro numero: ")
    numeros_invalidos()
    limite()
    #Verificar se os números estão corretos
    if numero == numeros[0]:
      numero = input("Digite o segundo numero: ")
      numeros_invalidos()
      limite()
      if numero == numeros[1]:
        numero = input("Digite o terceiro numero: ")
        numeros_invalidos()
        limite()
        if numero == numeros[2]:
          numero = input("Digite o quarto numero: ")
          numeros_invalidos()
          limite()
          if numero == numeros[3]:
            numero = input("Digite o quarto numero: ")
            numeros_invalidos()
            limite()
            if numero == numeros[4]:
              vitoria += 1
              print("Parabéns!!")
              print(f'Você acertou todos os 5 números: {numeros}')
              time.sleep(1)
              print(f'Você ganhou: {vitoria} veze(s)\ncomputador ganhou: {derrota} veze(s)')
              JogarNovamente()
            else:
              derrota += 1
              print("Errou!!")
              print(f'Os numeros certos eram {numeros}')
              time.sleep(1)
              print(f'Você ganhou: {vitoria} veze(s)\ncomputador ganhou: {derrota} veze(s)')
              JogarNovamente()
          else:
            derrota += 1
            print("Errou!!")
            print(f'Você ganhou: {vitoria} veze(s)\ncomputador ganhou: {derrota} veze(s)' )
            JogarNovamente()
        else:
          derrota += 1
          print("Errou!!")
          print(f'Você ganhou: {vitoria} veze(s)\ncomputador ganhou: {derrota} veze(s)')
          JogarNovamente()

      else:
        derrota += 1
        print("Errou!!")
        print(f'Você ganhou: {vitoria} veze(s)\ncomputador ganhou: {derrota} veze(s)')
        JogarNovamente()

    else:
      derrota += 1
      print("Errou!!")
      print(f'Os numeros certos eram {numeros}')
      time.sleep(1)
      print(f'Você ganhou: {vitoria} veze(s)\ncomputador ganhou: {derrota} veze(s)')
      JogarNovamente()

cadastro()
regras()
jogo()