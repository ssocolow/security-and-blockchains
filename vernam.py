# vernam cipher helper

# takes two strings of bits and returns their xor bitstring
def xor(key, m):
    n = [int(i) for i in list(m)]
    k = [int(i) for i in list(key)]

    return ''.join([str(j^k) for (j,k) in zip(n,k)])

k = '11000000'
t = xor(k,'10100110')
print(chr(int(t,2)))