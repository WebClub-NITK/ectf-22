# climb the HILL

Author : [Ragul N S](https://www.linkedin.com/in/ragulns/)

Flag: `CTF{y0u_h4ve_cl1m6ed_the_h1ll_here_1s_y0ur_fl4g}`

## Problem Statement

> \>increasing altitude...  
> \>z3{ryu0kdhhxwuph__oin4}{h5cn78y6a{obebxbh932j  
> \>6 24 11  
> \>12 13 10  
> \>20 17 15  
Flag format: CTF{...}

Proposed difficulty level: Easy

## Solution

We can get a hint from the Description and the name of the Challenge that it is **Hill Cipher**.

**The basic idea behind the Encryption Scheme is :**
* Select alphabet containting ***N*** letters.

| Letter |a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|0|1|2|3|4|5|6|7|8|9|{|}|_|
|--------|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
| Number |0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31|32|33|34|35|36|37|38|39|

* Use an ***n* x *n* invertible matrix (modulo *N*)** (where ***N*** is the total number of letters in the alphabet) as the key.
* Multiply each block of ***n*** plaintext letter numbers mapped to the respective letters with it.

**The Decryption Scheme is :**
* Select the same alphabet containting ***N*** letters. (In this challenge we have to guess the alphabet map from the ciphertext)
* Find the **inverse** of the given key matrix.
* Use the inverted ***n* x *n* matrix (modulo *N*)** as the key.
* Multiply each block of ***n*** ciphertext letter numbers mapped to the respective letters with it.

The [encrypt.py](https://drive.google.com/file/d/1vkiJrnVG6z-Lwp7E0AtI4a7j5cDCzJFM/view?usp=sharing) file has the code for converting the plaintext into the cipher text and the [decrypt.py](https://drive.google.com/file/d/1flufIqaFNKnnjs2XHpBAQed7yqCY3nl-/view?usp=sharing) has the code for converting cipher text to plain text. The key and the values for plaintext and ciphertext are hardcoded in the program.
