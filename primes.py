"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def isPrime(number):
    if ((number/2)%2 == 0): return False   
    
    half = number//2
    
    for i in range(2, half):
        if(number%i == 0):
            return False
        
    return True


def primes(number_of_primes):
    if(number_of_primes <= 0):
        raise ValueError("No numbers <= 0")
    
    list = []
    
    currentNumber = 2
    
    while len(list) < number_of_primes:
            
        if(isPrime(currentNumber)):
            list.append(currentNumber)
            
        currentNumber += 1
        
    return list