'''
Português: Há múltiplas maneiras de calcular o todos os números primos até N, tanto de maneiras recursivas
quando lineares. Embora *não recomendável* o uso de função recursivas para o cálculo de números primos
- e de fato, a partir de 1k recursion depth Python automaticamente identifica como um runtime error -,
nesse caso em particular, a diferença de complexidade O( ) entre a versão recursiva e a linear é trivial.
Como terceiro exemplo, incluí o Crivo de Eratóstenes, um algoritmo simples, embora não o mais eficiente,
com complexidade O(N log(N log)), ou seja, melhor que os dois acima.

English: There are multiple ways to calculate all primes up to N, both with recursive functions aswell as linear
ones. Although it is *not advised* to use recursion to calculate primes - and in fact Python throws a runtime
error whenever the max 1k recursion depth is exceeded - in this particular case, the O () complexity between the
recursive and linear versions is trivial. As a third example, Ive included the Sieve of Eratosthenes, a simple
algorithm, not currently the most efficient one, which takes O(N log(N log)) to find all primes < N.
'''

#O(n) --- retorna NONE se divisor > 1 for encontrado para N
#O(n) --- returns NONE if a divisor > 1 is found for N
def prime(n):
    for i in range(2, n - 1):
        if n % i == 0:
            return
    return n

#O(2^n) --- se N <= 1; chama a si mesmo até que N = 1, e para cada vez, se prime(n) == True, adiciona n ao final da lista primesList
#O(2^n) --- if N <= 1; calls itself until N = 1 and for each time, if prime(n) = True, appends n to the end of the list
def recursive(n):
    if n > 1:
        primesList = recursive(n - 1)
        if prime(n):
            primesList.append(n)
        return primesList
    return []

#O(2^n) --- se N <= 1, retorna uma lista vazia; senão realiza um loop de 2 até N - 1 e retorna N se prime(n) = True
#O(2^n) --- if N <= 1, returns an empty list; otherwise loops from 2 to N - 1, and returns N if prime(n) = True
def linear(n):  
    if n > 1:
        return [n for n in range(2, n + 1) if prime(n)]
    return []

#O(N log(N log)) --- se n <= 1, retorna uma lista vazia; senao inicializa uma lista de booleans de tamanho N + 1 chamada primesList; primesList[0] e [1] recebem False, como nao 
#podem ser primos; realiza um loop de 2 a raiz de n + 1, pois todo numero nao primo i < n deve ter ao menos um fator menor ou igual a raiz de n; se i for primo, todos
#multiplos de i < n sao marcados como False, ou seja, nao primos; retorna uma lista com todos os casos onde i e True em primesList[i]

#O(N log(N log)) --- if n <= 1, returns an empty list; otherwise initializes a list of booleans of the size N + 1, called primesList; primesList[0]and [1] are False, as they
#cannot be primes; loops from 2 to the square root of n+1, since every non prime number i < n must be at least one of its factors as equal or less than n; if i is prime,
#all its multiples are declared False, that is, not prime; returns a list with all cases where i is True in primesList[i]
def eratosthenesSieve(n):
    if n > 1:
        primesList = [True] * (n + 1)
        primesList[0] = primesList[1] = False

        for i in range(2, int(n**0.5) + 1):
            if primesList[i]:
                for j in range(i * i, n + 1, i):
                    primesList[j] = False
        return [i for i in range(2, n + 1) if primesList[i]]
    
    return []