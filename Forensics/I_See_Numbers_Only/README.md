# I see numbers only

Author: [Shashank D](https://github.com/shashank68)

Flag: `CTF{IT5ALL1NNUMBER5}`

## Problem Statement

Mr. Codeshankar was trying to suspiciously send some data to mafia leader Mr. Pythonarayan. Thankfully he was caught red-handed along with the data he was trying to send. But what was he actually sending though?

## Relevant files / links

- [Secret Data](https://drive.google.com/file/d/1kL7XxBsk_jKo7B7i8XU1Wj6vdd3RGxu7/view?usp=sharing)


## Solution

The given file is a tar archive file compressed with XZ [tar.xz file not a zip file :) ]. After extraction, we see that there are 5 spreadsheets each of almost same size and same dimension of filled numbers. The numbers range from 0 to 255 in each of the cell. This clearly hints that these are pixel values of an image which has been split uniformly into 5 parts. 

So each column of 3 cells of the sheet must be coloured with RGB values as mentioned in the cell. Finally merging the sheets horizontally will give the complete picture of flag text

- [Merged Spreadsheet](https://docs.google.com/spreadsheets/d/1TKpQVfVWqMQGfnvIGIgAbfI84YcBBDZR/edit?usp=sharing&ouid=115809332496163913440&rtpof=true&sd=true)
