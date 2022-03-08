# I can do this all day.
Author: Vinayak Vatsalya J

Flag: `CTF{d3cry471ng_nu3l34r_c0d35}`

## Problem Statement

<b>Tony Stark: </b> a hacker who's faster than ultron? he could be anywhere GLOBAL. And as this is the center of everything, I'm just a REGULAR guy looking for a needle in the world's biggest haystack.

<b>World Hub Tech:</b>  How do you find it? \<with puzzled EXPRESSION>

<b>Tony Stark: </b> pretty simple. you bring a magnet.
  
Flag format: CTF{...}

## Relevant files / links

- [icandothisallday.zip](https://drive.google.com/file/d/1DsD8FrZ0rFgAwsyxkDJx83SLECjjnfN8/view?usp=sharing)

## Hint 
 - Google the words in uppercase.
 - [grep](https://explainshell.com/explain?cmd=grep)

## Solution
On unzipping icandothisallday.zip , we get 318 txt files, each one having some text in it. Only one text file contains the flag in the given format.
- The [grep](https://explainshell.com/explain?cmd=strings+*+%7C+grep+CTF) command , `strings * | grep CTF` would give the flag. <br>
- The flag can also be found using a simple python script : 
```python
import os 
for file in os.listdir('icandothisallday/'):
    f = open(f'icandothisallday/{file}')
    text = f.readline()
    if 'CTF' in text:
        print(text)
        break    

```