# Shakespeare and Encoding

Author: Adarsh Kishore <br />
Flag: <code>CTF{Y0U-too-Bru1uS}</code>

## Problem Statement

Brutus planned to kill Caesar. However, he hesitated, for he was
afraid that Caesar would say
 <code>01000100 01010101 01000111 01111100 01011010 00110001 01010110 00101110 01110101 01110000 01110000 00101110 01000011 01110011 01110110 00110010 01110110 01010100 01111110</code>. What did he say?

## Hints

1. Caesar would obviously say it in English
2. Why is Caesar here anyway?

## Solution

This problem is based on Caesar cipher + ASCII encoding. The code on
decoding  gives <code>DUG|Z1V.upp.Csv2vT~</code>. Now we can see that
DUG is CTF shifted by 1 character. Applying the caesar cipher with a
shift of 1, we get the flag. The solution is [here](solution.py).
