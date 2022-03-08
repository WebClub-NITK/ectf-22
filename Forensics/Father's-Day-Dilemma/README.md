# Father's Day Dilemma

Author: [Pratik Jallan](https://www.linkedin.com/in/pratik-jallan-yukino2002/)

Flag: `CTF{PJCOOL}`

## Problem Statement

Samuel had two children, Dot and Dash, who were extremely fond of numbers. However, they only liked numbers that were greater than 8. For some reason, Dot used to find the number 10 espcially pleasing, it was the same for Dash with the number 12. On Father's day, they came up with a problem for their father to enjoy. Looking at his children, Samuel knew that the problem wouldn't be easy to solve and at the same time would involve numbers.

Can you help Samuel find the hidden message in the file? The answer format is CTF{hidden message}, all caps, no spaces.

## Relevant files / links

- [Google Drive link](https://drive.google.com/drive/folders/11QNi39FPdXKt4qxMnw42yKX9sEYi0fx5?usp=sharing)

## Hint

1. While you might feel lazy to read the entire text, in the end, you might miss out on something... 

## Solution

The problem primarily involves `White Space Steganography` and use of `Morse Code` encoding. Steganography is a method of hiding secret data, by embedding it into some file, in this case, using blank spaces to hide the morse code in the html file. It is one of the methods employed to protect secret or sensitive data from malicious attacks. Morse code is a method used in telecommunication to encode text characters as standardized sequences of two different signal durations, called dots and dashes, or dits and dahs.

The second last paragraph of the webpage gives us the hint that some form of encoding (that uses symbols) is involved. The last paragraph hints the person to open the same file in a different manner, that is the html code for the webpage and observe the structuring of the sentences. Any text editor can be used for this purpose, although something like VS Code would make it much easier. The hint tells the user to check towards the end as well.

Now, coming to problem statement, we already know that some form of encoding is involved. It is a clear indication of Morse code. The names used indicate so, `Samuel, inventor of morse code` and his children, `Dot and Dash, are the symbols used in morse code`.

We have also been given 3 numbers, `8, 10 and 12`. Associating Dot with 10 and Dash with 12, we see that the odd structuring of sentences is done at either 10 white spaces or 12 white spaces. We are ignoring anything less than equal to 8 as both Dot and Dash dislike such numbers. Basically, all the `10 white spaces correspond to one dit` while `12 spaces correspond to one dah`. All the div tags give us one character each, encoded in morse code. Which makes our final answer as `PJCOOL`.
