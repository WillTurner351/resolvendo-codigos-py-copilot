# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

operaçao = input("Digite a operação que deseja realizar (+,-,*,/:)")

if operaçao == '+':
    print(num1 + num2)
elif operaçao == '-':
    print(abs(num1 - num2))    
if operaçao == '*':
    print(num1 * num2)
elif operaçao == '/':
    print(num1 / num2)
else:
    print("Operação inválida")