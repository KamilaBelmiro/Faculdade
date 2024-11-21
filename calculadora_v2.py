saida = ''; # Vari�vel para controlar o loop principal

def adicao(numero1, numero2):  
    soma = numero1 + numero2, 
    return soma;


def subtracao(numero1, numero2):
    diferenca = numero1 - numero2,
    return diferenca;

def multiplicacao(numero1, numero2):
    produto = numero1 * numero2,
    return produto;

def divisao(numero1, numero2):
    
    if numero2== 0:
        return "N�o foi poss�vel realizar a divis�o por 0"
    
    else: 
      
        return numero1 / numero2;
# Fun��es subtracao, multiplicacao e divisao possuem estrutura similar, com devidas altera��es

def calculadora(numero1, numero2, operacao):
    
     if operacao in ['+', 'adicao']:
        resultado = adicao(num1, num2),

     elif operacao in ['-', 'subtracao']:
        resultado = subtracao(num1, num2),

     elif operacao in ['*', 'multiplicacao']:
        resultado = multiplicacao(num1, num2),

     elif operacao in ['/', 'divisao']:
        resultado = divisao(num1, num2),

     else:
        resultado = "Opera��o inv�lida."
     return resultado;
    
saida = '';

# Loop principal para realizar m�ltiplos c�lculos
while saida.lower() != 'n':
    # Obter os n�meros e a opera��o do usu�rio
    num1 = float(input("Digite o primeiro n�mero: "))
    num2 = float(input("Digite o segundo n�mero: "))
    operacao = input("Digite a opera��o (+, -, *, / ou seu nome completo): ")

    # Chamar a fun��o calculadora e imprimir o resultado
    resultado = calculadora(num1, num2, operacao)
    print("Resultado da opera��o:", resultado)

    # Perguntar se o usu�rio deseja continuar
    saida = input("Deseja continuar? (S/N): ")
    if saida.lower() not in ['s', 'n']:
        print("Resposta inv�lida. Por favor, digite S para continuar ou N para sair.")
    


