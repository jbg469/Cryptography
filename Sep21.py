#Sept 28
p = 23
g = 5

def next_in_sequence (n, g, p):
    return (g*n) % p
def print_group(g,p):
    n = g
    for _ in range(p-1):
        n = next_in_sequence(n,g,p)
        print(n,end=' ')
    print()
print_group(g,p)

import secrets

p = 1499
g = 2

a=secrets.randbelow(p-2) + 2
A= pow(q,a) % p
B = 147
V = pow(B,a) % p
import hashlib 

hashlib.sha512(bytes(V)).digest()[16]
