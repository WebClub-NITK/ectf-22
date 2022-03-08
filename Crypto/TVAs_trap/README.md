# TVA's Trap

Author: Vinayak Vatsalya J

Flag: `CTF{w3c-ctf-z0z2_3ry9t0}`

## Problem Statement
  
Nadia is caught in a time loop as the guest of honor at a seemingly inescapable party one night in New York City. In order to get out she has to decode the following text message she gets. The TVA being noobs don’t understand that just encoding is not exactly secure. Can you get the flag and help Nadia get to base ?
  
Flag format: CTF{...}

## Relevant files / links

- [8-6-4.txt](https://drive.google.com/file/d/1LL2W5-g9oKxUI5P8rSCCOyLc7P6TFDA0/view?usp=sharing)

## Hint 
 - Fall Down 7 Times Get Up 8 <br><br>![Fall Down 7 Times Get Up 8](https://media.giphy.com/media/3o6ZsYiDWgEk6UgshO/giphy.gif)
 - Reverse search the first line of this challenge to get a clue. 

## Solution
The flag can be obtained decoding the text which is encoded in base64 in `8-6-4.txt` file 8 times (each time the new text to be decoded is the previous decoded text).<br>
- [base64 decoder](https://www.base64decode.org)
                    
