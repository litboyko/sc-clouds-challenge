import numpy as np
'''
Português: O cálculo do enésimo número da sequência fibonacci pode ser realizado desde formas extremamente simples, mas menos eficientes,
até de jeitos mais avançados que produzem melhores resultados para números mais altos. Recursão se demonstra perigoso ao arriscar exceder
o max recursion depth, se feito da primeira maneira, mas pode ser mais eficiente dependendo da aplicação, como visto na exponenciação de matrizes.
Em cenários reais, os dois últimos exemplos seriam mais praticáveis. O último, por exponenciação de matrizes, é também muito utilizado em programação competitiva.

English: Calculating the Nth number on the fibonacci sequence can be done in simple, less efficient ways, aswell with more advanced methods that
yield better results with higher numbers. Recursion may risk violating the python recursion depth, and can be highly inefficient if done incorrectly,
but the last example shows it can also yield the best results. In real world cases, the last two are the only ones that can be applied. The last one,
done by matrix exponentiation, is often used in competitive programming
'''

#O(2^n) --- se n > 1, soma recursivamente n-1 e n-2 e retorna o resultado se n >= 0, retorna n; senao nada é retornado]
#O(2^n) -- if n > 1, recursively sums n-1 and n2 and returnsthe result if n >= 0 returns n; otherwise nothing is returned
def recursive(n):
    if n > 1:
        return recursive(n-1) + recursive(n-2)
    elif n >= 0:
        return n

#O(n) --- declara A e B, 0 e 1 respectivamente; se n >= 0 realiza loop n vezes, designando o valor de B a A, e A + B a B sucessivamente, retorna A ao fim do loop
#O(n) -- declares A and B, 0 and 1 respectively; if n >= 0 loops n times, assigning the value of B to A, and A + B to B repeatedly, returns A at the end of the loop
def linear(n):
    a, b = 0, 1
    if n >= 0:
        for i in range(n):
            a, b = b, a + b
        return a

'''
O(log n)
Matriz: Se n > 1, uma matriz base [[1, 1], [1, 0]] é declarada. Base é passada como primeiro argumento da função de exponenciação, e n-1 como seu expoente. Retorna
o primeiro elemento da primeira linha da matriz retornada pela funcao power; se n >= 0, retorna n.
Power: Se o expoente (n-1) for 0 ou 1, retorna a matriz, sem realizar exponenciação. Se o expoente (n-1) for par, chama a si mesma recursivamente, com a exponenciação
da matriz como nova base, e o expoente subtraido em 1 dividido pela metade ((n - 1)/2) e arredondado. Se nenhum dos casos interior for verdadeiro, a matriz
é multiplicada pelo resultado da função power chmada recursivamente, que toma a exponenciação da matriz como base, e (n-2)/2 arredondado como expoente.

O(log n)
Matrix: if n > 1, the matrix [[1, 1], [1, 0]] is declared as base. This matrix is passed as the first argument of the power function, and n-1 as its exponent. Returns the first element
of the first row of the matrix returned by the power function. If n >= 0, returns n.
Power: If the exponent (n-1) is 0 or 1, returns the matrix. If the exponent is even, recursevely calls itself, multiplying the matrix by itself and using as new base, and (n - 1)/2,
rounded down, as the new exponent. If exponent is neither even, nor == 0 or 1, multiplies the matrix for the result of the recursevely called power function (which uses the squared matrix
as the new base, and (n-2)/2, rounded down, as the new exponent).
'''

def power(base, exponent):
    if exponent == 0 or exponent == 1:
        return base
    if exponent % 2 == 0:
        return power(np.dot(base, base), exponent // 2)
    else:
        return np.dot(base, power(np.dot(base, base), (exponent - 1) // 2))

def matrix(n):
    if n > 1:
        base = np.array([[1, 1], [1, 0]], dtype=object)
        result = power(base, n - 1)
        return result[0][0]
    elif n >= 0:
        return n