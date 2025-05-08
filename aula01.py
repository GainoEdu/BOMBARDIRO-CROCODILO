import os
os.system("cls")

#cpf=49093999842
#idade=98
#nome=eduardo                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
#print(f"qual seu nome? \n meu nome é {nome}")
#print(f"qual sua idade? \n minha idade é {idade}")
#print(f"qual seu cpf? \n meu cpf é {cpf}")

#dia=24
#print("bom dia",f"hoje é dia {dia}",sep="!",end="!!")
#print("\n")
#numero=10
#numero2=input("digite um numero: ")
#print("o tipo de numero é,", type(numero2))
#soma=numero+int(numero2)
#print(f"soma de {numero} + {numero2} = ", soma)


#liçaum 3
#num1=2025
#num2=input("digite o seu ano de nascimento:")
#type(num2)
#subtraçao=num1-int(num2)
#print(f"sua idade é {num1} - {num2} = ", subtraçao)

#liçaum 1

#num1=input("manda um numero meu chapa:")
#num2=input("manda outro numero meu chapa:")
#subtraçaum=int(num1)*int(num2)                  
#print(f"o resultado de {num1} * {num2}", subtraçaum)

#liçaum 2

#num1=float(input("manda um numero lixo:"))
#antecessor=num1-1
#sucessor=num1+1
#print(f"o antecessor é: {antecessor} e o sucessor é: {sucessor}")

#MERCADINHOOOOOO

#print("-_-_-_-_-MERCADO DO DU-_-_-_-_-")
#produto1=input("digite o nome do produto:")
#preço1=float(input("digite o preço do produto:"))
#desconto1=float(0.10 * preço1)
#produto2=input("digite o nome do outro produto:")
#preço2=float(input("digite o preço do produto:"))
#desconto2=float(0.25 * preço2)
#print(f"preço do produto com desconto: {desconto1}\n"f"preço do segundo produto com desconto: {desconto2}")
#total = round(preço1-desconto1,2) + round(preço2-desconto2,2)
#print("-_-_-_-_-VALOR DO SEUS PRODUTOS-_-_-_-_-")
#print(f"valor final da sua compra: {total}")

#tarefa das maças

#qnt = int(input("quantas maças deseja levar?")) 

#if qnt < 12 :
    #calc = qnt * 0.30
    #print("o total da sua compra ficou: RS$:", calc)

#else:
    #calc = qnt * 0.25
    #print("o total da sua compra ficou: RS$:", calc)


#letra=input("digite uma letra de A ate E:")

#if letra in "ABCDE":
#    print("maiusculo")
#else:
#   letra in "abcde"
#    print("minusculo")


#nota boletim

#nota1 = float(input("primeira nota:").replace(",","."))
#nota2 = float(input("segunda nota:").replace(",","."))
#merdia = (nota1+nota2)/2
#print(f"sua nota é {merdia}")
#if merdia < 5:
#    print("reprovado")
#elif merdia < 7:
#    print ("recuperação") 
#elif merdia >= 7:
#    print("aprovado")


#IMC
 
# peso = float(input("qual seu peso?:"))
# altura = float(input("qual sua altura:"))
# imc = (peso / (altura * altura))
# if imc < 17:
#     print(f"{imc}\n vara de cutucar estrela")
# elif imc < 18.49:
#     print(f"{imc}\n quase vara de cutucar estrela")
# elif imc < 24.99:
#     print(f"{imc}\n normal mas vc é anormal")
# elif imc < 29.99:
#     print(f"{imc}\n esta gordinho ein, bola de bilhar")
# elif imc < 34.99:
#     print(f"{imc}\n esta gordo não? bola de basquete")
# elif imc < 39.99:
#     print(f"{imc}\n saturno é vc?")
# else:
#     print(f"{imc}\n VOCE È MUITO GORDOOOOOOOO")        


#auto-car

#salario_atual=float(input("fale seu salario:"))
#if salario_atual <= 2779.99:
#    percentual=0.20
#elif salario_atual <= 6999.99:
#    percentual=0.15
#elif salario_atual <= 14999.99:
#    percentual=0.10
#else:
#    percentual=0.05

#va=salario_atual*percentual
#ns=va+salario_atual

#print(f"SALARIO ANTES DO REAJUSTE {salario_atual} ")
#print(f"PERCENTUAL DO AUMENTO APLICADO {percentual}")
#print(f"VALOR DO AUMENTO APlICADO {va}")
#print(f"NOVO SALARIO{ns}")


#CASE
#print("1-segunda-feira \n 2-terça-feira \n 3-quarta-feira \n 4-quinta-fera \n 5-sexta-feira \n 6-sabado-feira \n 7-domingo-feira")
#dia=input("digite um dia da semana:")
#
#match dia:
#
 #  case "1":
 #       print("segunda")
 #  case "2":
 #       print("terça")
 #  case "3":
 #       print("quarta")
 #  case "4":
 #       print("quinta")
 #  case "5":
  #      print("sexta")
  # case "6":
 #       print("sabado")
 #  case "7":
  #      print("domingo")
 #  case _:
 #      print("digite um dia valido animal")

#MATCH CASE


#print(" MUNDO DO CLULAR \n 1-IPHONE 15 - R$:5000.00 \n 2-XIAOMI REDMI 13 PRO PLUS 512GB - R$:2500.00 \n 3-SANSUNG S25 ULTRA 265 GB - R$:6999,99 \n FRETE:SP->10.00 \n       MG->15.00 \n       RS->20.00")
#celular=input("qual smartphone deseja?")
#match celular:
#    case "iphone":
 #       print("sue celular é um iphone")
#        iphone=5000
#    case "xiaomi":
#        print("seu celular é um xiaomi")
 #       iphone=2500
#    case "sansung":
#        print("seu celular é um sansung")
#        iphone=6999.99
#região=input("qual sua região?")
#match região:
#    case "sp":
#        print("seu frete ficara 10.00")
#        sp=10
#    case "mg":
#        print("seu frete ficara 15.00")
#        sp=15
#    case "rs":
#        print("seu frete ficara 20.00")
#        sp=20
#print(f"O valor total vai ser R${iphone+sp}")

#pedra, papel ou tesoura
import random
print("JOGO DO PEDRA, PAPEL OU TESOURA")


papel = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

pedra = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


tesoura = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""
pppt=input("escolha pedra papel ou tesoura:")
1 = papel
2 = pedra
3 = tesoura
match pppt:
    case 1:
        print(f"{papel}")
    case 2:
        print(f"{pedra}")    
    case 3:
        print(f"{tesoura}")
ppt = random.randit(1,3)

match ppt:
    case 1:
        print(f"{papel}")
    case 2:
        print(f"{pedra}")
    case 3:
        print(f"{tesoura}")































































































































