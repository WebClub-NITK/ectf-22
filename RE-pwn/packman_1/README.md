# Packman 1

Author: Sudesh Gowda J

Flag: CTF{ee_lo_p3ll3t_kh4o}

## Problem Statement

Packman found this binary pellet but he is "sus" about this. Help the Packman "unpack" the situation.


## Relevant files / links

- [chall](https://drive.google.com/file/d/1xhFx0atxYlyEHYfLeZlYqfL8hRRbbk1U/view?usp=sharing)

## Hint

Go to Ms.Jefferson

## Solution

First extract the given zip file. It will contain a binary file. Running <code>file</code> command on the given binary reveals that the given file is a firmware image. Now using <code>binwalk -e</code>, we can unpack the given firmware. 

Hint tells us to go to Ms.Jefferson(jffs). There will be a <code>.jffs2</code> file in the extracted folder. Use tools like [jefferson](https://github.com/sviehb/jefferson) to extract this jffs file. Searching in the extracted file system will lead to a folder named sus which will contain the flag in a file named <code>flag.txt</code>.
