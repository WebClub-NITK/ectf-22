# Locked Out

Author: [Vinayak Vatsalya J](https://github.com/vinayakj02)

Flag: `CTF{r0n_4D1_130N4rd}`

## Problem Statement
  
 Coulson is locked out of Ragtag. Can you help him get back to BASE by finding the flag. He found this image in BIN. 
  
Flag format: CTF{...}

## Relevant files / links

- [flag.png](https://drive.google.com/file/d/1Tx7V-x3slP2hTW-JXIaNLq0X6JTxXd90/view?usp=sharing)


## Solution
 - The QR code gives a string encoded in base64. After [decoding](https://www.base64decode.org) this we get a link to a text file.<br>
 - This is in binary. After [converting binary to text](https://www.rapidtables.com/convert/number/binary-to-ascii.html), we get values of n , c and e (RSA). To find the factors of n ( p and q ) [this tool](http://factordb.com/) can be used.
 Using p and q values, d can be found using following script.
 ```python
 c = 7424699238646955201370695213431987671142812230143306867560482933056266299380926684689129315498363439046922143979269386180477235672715428337919573885741855
n = 14783703403657671882600600446061886156235531325852194800287001788765221084107631153330658325830443132164971084137462046607458019775851952933254941568056899
e = 0x10001

p = 121588253559534573498320028934517990374721243335397811413129137253981502291629 
q = 121588253559534573498320028934517990374721243335397811413129137253981502291631   #from factordb

phi = (p-1)*(q-1)

from Crypto.Util.number import inverse 
d = inverse(e, phi)
m = pow(c,d,n)

import binascii
print(binascii.unhexlify(hex(m)[2:])) #gives the flag as : 'CTF{r0n_4D1_130N4rd}'

``` 
                    
