# Plain Sight

Author: Kavya Bhat

Flag: `CTF{p1k@chu}`

## Problem Statement

TJ loves wearing his invisibility Cloak and hiding in Plain Sight. He also likes making lists of his favourite Pokemon. TJ asked you for the flag in exchange for a poster of his favourite Pokemon. Here's the poster, can you uphold your end of the bargain?

## Relevant files / links

- [poster.jpg](./poster.jpg)

## Hint

- TJ’s Cloak was made in a Factory that hides many things in Plain Sight.
- Turns out TJ's poster can also hide items..

## Solution

Examine the image using `binwalk`, and you will find that there is a zip file hidden along with the image. Extract it using `binwalk -e poster.jpg`. Unzipping this file reveals a short list of Pokemon.

The words Cloak and Plain Sight provide clues to the next step. The hint indicates that the word Factory would help too. Googling these words should lead us to [Cloakify](https://github.com/TryCatchHCF/Cloakify), an open source tool that uses text-based steganography to convert a file into a list of strings. 

Clone the repo and copy the obtained `list.txt` file into the directory. Run Cloakify using `python cloakifyFactory.py`, which gives a list of options. On choosing option 2, `Decloakify`, you get a list of ciphers from which you choose one to decode the given text file. With all the references to Pokemon, the obvious choice would be `pokemongo`.  

The decoded file contains the flag `CTF{p1k@chu}` as plaintext.