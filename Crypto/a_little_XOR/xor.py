# flag = 'ctf{@_b1t_0f_X0R}'
# key = 241

# plaintext ---> binary ASCII
def toBinary(text):
    final = ""
    for c in text:
        temp = bin(ord(c))[2:]
        final += temp + " "
    return final

# binary ASCII ---> cipher
def encrypt(binary, key):
    final = ""
    for c in binary.split():
        temp = bin(int(c, 2) ^ key)[2:]
        final += temp + " "
    return final

# cipher ----> binary ASCII
def decrypt(binary, key):
    final = ""
    for c in binary.split():
        temp = bin(int(c, 2) ^ key)[2:]
        final += temp + " "
    return final

# binary ASCII ---> plaintext
def toString(binary):
    final = ""
    for c in binary.split():
        temp = int(c, 2)
        final += str(chr(temp % 128))
    return final

# xors str1 binary and str2 binary
def xor(str1, str2):
    final = ""
    t1 = str1.split()
    t2 = str2.split()
    for i in range(len(t1)):
        c1 = t1[i]
        c2 = t2[i]
        c = bin(int(c1, 2) ^ int(c2, 2))[2:]
        final += c + " "
    return final

if __name__ == "__main__":
    p = "10010010 10000101 10010111 10001010 10110001 10101110 10010011 11000000 10000101 10101110 11000001 10010111 10101110 10101001 11000001 10100011 10001100"
    print(p)

    p2 = "10010111 10011110 10000011 11011100 10101110 10010000 10011101 10011101"
    c12 = "110010 11101 10111 1001100 101100 10100 11110 1001"
    c1 = "Treasure"

    c2 = (xor(c12, toBinary(c1)))

    k = int(xor(c2, p2).split()[0], 2)

    print(k)
    print(toString(decrypt(p, k)))
