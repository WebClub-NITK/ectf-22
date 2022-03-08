def caesar(word, key):
    newword = ""
    for c in word:
        newword += chr(ord(c) + key)
    return newword


def toString(code):
    newword = ""
    for c in code.split():
        temp = int(c, 2)
        newword += chr(temp)
    return newword


encrypted = "01000100 01010101 01000111 01111100 01011010 00110001 01010110 00101110 01110101 01110000 01110000 00101110 01000011 01110011 01110110 00110010 01110110 01010100 01111110"
key = 1

print(caesar(toString(encrypted), -key))
