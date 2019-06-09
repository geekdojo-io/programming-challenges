# Sieve of Eratosthenes

Technique to find all prime numbers up to any given limit.

#### Python

```py
def get_primes(limit):
  P = [True]*(limit + 1)
  P[0] = P[1] = False # Mark 0 and 1 as not prime
  prime = 2 # Let's start with 2 as a prime number
  while prime < len(P):
    # Mark multiples of prime as not primes.
    for i in range(2*prime, len(P), prime):
      P[i] = False
    # Find next prime
    prime += 1
    while prime < len(P) and not P[prime]:
      prime += 1
  return P
  
P = get_primes(100)
# Test result
assert P[5] == True
assert P[11] == True
assert P[16] == False
```

### Reference
- [Wikipedia - Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
