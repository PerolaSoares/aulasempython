# 1)Escrever um programa em Python para exibir os números de 1 até 50 na tela.
x = 1
while x <= 50:
    print(x , end=',')
    x = x + 1

#2) Faça um programa em Python que imprima os 10 primeiros números.
x = 0
while x <= 10:
    print(x)
    x += 1

#3) Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, …, 1, 0 e Fogo! na tela.
x = 10
while x >= 0:
    print(x)
    x = x - 1
print("Fogo!")

#4) Faça um programa em Python para imprimir de 1 até o número digitado pelo usuário, mas,dessa vez, apenas os números ímpares.
var = int(input("Digite o último número a imprimir:"))
x = 1
while x <= var:
    print(x)
    x = x + 2

#5) Reescreva o programa anterior para escrever os 10 primeiros múltiplos de 3.
multiplo= 30
x = 3
while x <= multiplo:
    print(x)
    x = x + 3

#6) Altere o programa anterior para exibir os resultados no mesmo formato de uma tabuada: 2x1 = 2,2x2 = 4, …
tabu= int(input("Tabuada de:"))
x = 1
while x <= 10:
    print(f"{tabu} x {x} = {tabu * x}")
    x = x + 1

#7) Crie um programa em Linguagem Python que solicite a senha de um usuário e depois, peça pra digitar novamente até que as duas senhas sejam correspondentes.
usuario= input("Digite a senha: ")
senha = input("Confirme a senha: ")
while usuario != senha:
    print("Senha errada, tente novamente.")
    usuario = input("Digite a senha: ")
    senha = input("Confirme a senha: ")
print("senha correta, parabéns!")

#8) Faça um programa em Python que leia uma quantidade de números inteiros digitados pelo usuário,até que o usuário digite 0. Ao final, mostre a soma de todos os números digitados.

soma=0
numero=int(input("Digite um número: "))
while numero != 0:
    soma +=numero
    numero=int(input("Digite um número:: "))
print("Soma = ",soma)
      

#9) Faça um programa em Python que leia uma quantidade de números inteiros e positivos digitados pelo usuário, até que o usuário digite 0. Ao final, informe o maior número digitado o menor número digitado e a quantidade de números pares.

maior=-1
numero=int(input("Entre com um número inteiro e positivo:"))
while numero>=0:
  if numero>maior:
    maior=numero
    numero=int(input("Entre com um número inteiro e positivo:"))
print("o número", maior,"é o maior número digitado")

#10) Faça um programa em Python que permita que o usuário insira valores de produtos comprados por um cliente qualquer. O programa deve encerrar quando o usuário digitar “SAIR”. Se o usuário digitar um valor negativo não deve ser processado e um novo valor deve ser solicitado como entrada. Ao final, informe o valor total a pagar, lembrando que, caso as vendas ultrapassem o total de R$3.000,00, deverá ser aplicado um desconto de 12%. Mostrar ao final valor total, o valor do desconto e o valor líquido.


#11) Faça um programa em Python para calcular a soma e a média de x números inteiros inseridos pelo usuário. Digite -1 para terminar.

print("Insira os números. Digite -1 para sair: ")
contador = -1
soma = 0.0
num = 1

while num != -1:
   num = int(input(""))
   soma = soma + num
   contador += 1
if contador == -1:
   print("Digite alguns números")
else:
    print(" Média= ", soma/(contador-1))
    print("Soma dos números= ", soma)