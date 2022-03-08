
# THE CAT KNOWS THE CULPRIT

Author: Vishnu Sai

Flag: `CTF{It_1s_D0UG_JUdY}`

## Problem Statement

Detective Jake Peralta and his partner Charles Boyle are assigned a Grand Larceny case, by their captain Raymond Holt. 
Upon their arrival to crime scene they find that there are no clues for them to catch the victim, so they leave the crime scene and at the 
~~exif~~ exit door they find a [Image](https://drive.google.com/file/d/17jCxfhCdkMm3wA1WI3MdqaGIGNTt51RL/view?usp=sharing) along with a note saying **"THE CAT KNOWS THE CULPRIT."** 

## Relevant files / links

- [IMAGE FOUND](https://drive.google.com/file/d/17jCxfhCdkMm3wA1WI3MdqaGIGNTt51RL/view?usp=sharing)


## Solution

The EXIFDATA in the given Image has been changed ( Read more at [here](https://linuxhint.com/image-metadata-editors-linux/#:~:text=ExifTool%20is%20a%20command%20line,tags%20as%20per%20Exif%20standards)) such that it contains the flag and participant can find 
the flag in Comments Tag. The participants can take a hint from " ~~exif~~ exit " part.  
