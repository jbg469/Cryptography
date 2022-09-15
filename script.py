import hashlib

z = b'x\00' * 8
print(z)
hc = hashlib.sha256()
hc.update(z)
out = hc.digest()
print (out)
for ch in out:
     print (hex(ch),end='')
nicer=''
for ch in  out:
    nicer=nicer+hex(ch)[2:]
print (nicer)
# Entropy - A random 128 bit value can never have more that 128 bits of entropy in a system
import random
import secrets 

seed = secrets.randbits(64)
random.seed(seed)
