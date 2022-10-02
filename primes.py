"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if(number_of_primes <= 0):
        raise ValueError
    
    list = []
    
    count = 2
    
    while len(list) < number_of_primes:
        isPrime = True
        
        for i in range(2, count):
            if(count%i == 0):
                isPrime = False
                break
            
        if(isPrime):
            list.append(count)
            
        count += 1
        
    return list