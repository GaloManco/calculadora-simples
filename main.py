
# menu
print('Escolha a operação, \n( + ) Adição \n( - ) Subtração \n( / ) Divisão \n( * ) Multiplicação \n( ** ) Raiz')

# Escolhendo a operação
print('-'*20)
operacao = input("Operação: ")
print('-'*20)

# Escolha do números
num1 = int(input('Fist number: '))
num2 = int(input('Second number: '))

# Operaçao soma
if operacao == "+":
   soma = num1 + num2
   print(soma) 
