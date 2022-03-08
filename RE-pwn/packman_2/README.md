# Packman 2

Author: Sudesh Gowda J

Flag: CTF{ismartie}


## Note

This question should be accessible after solving Packman 1

## Problem Statement

Packman found out the sus thing in the pellet. Now help him to find the "password" for the "root" of this problem.

Flag format: CTF{password}

## Relevant files / links

- [chall](https://drive.google.com/file/d/1xhFx0atxYlyEHYfLeZlYqfL8hRRbbk1U/view?usp=sharing)


## Hint

Ask Mr.John in the shadows

## Solution

First extract the given zip file. It will contain a binary file. Running <code>file</code> command on the given binary reveals that the given file is a firmware image. Now using <code>binwalk -e</code>, we can unpack the given firmware.

Now we are required to find the root password. <code>/etc/shadow</code> is a text file that contains information about the system’s users' passwords(Given hint also mentions this). To obtain this, first extract <code>squashfs</code> file using <code>unsquashfs</code> command. Inside the extracted file system, we can find the shadow file inside <code>/etc</code> folder. Using tool like [John the Ripper](https://github.com/openwall/john) to crack the password, we get <code>ismartie</code> as password.
