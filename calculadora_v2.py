saida = ''; # Variável para controlar o loop principal

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
        return "Não foi possível realizar a divisão por 0"
    
    else: 
      
        return numero1 / numero2;
# Funções subtracao, multiplicacao e divisao possuem estrutura similar, com devidas alterações

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
        resultado = "Operação inválida."
     return resultado;
    
saida = '';

# Loop principal para realizar múltiplos cálculos
while saida.lower() != 'n':
    # Obter os números e a operação do usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, / ou seu nome completo): ")

    # Chamar a função calculadora e imprimir o resultado
    resultado = calculadora(num1, num2, operacao)
    print("Resultado da operação:", resultado)

    # Perguntar se o usuário deseja continuar
    saida = input("Deseja continuar? (S/N): ")
    if saida.lower() not in ['s', 'n']:
        print("Resposta inválida. Por favor, digite S para continuar ou N para sair.")
    


