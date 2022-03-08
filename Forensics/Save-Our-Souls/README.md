# Save Our Souls!

Author: [Pratik Jallan] (https://www.linkedin.com/in/pratik-jallan-yukino2002/)

Flag: `CTF{WE-NEED-REINFORCEMENTS}`

## Problem Statement

WAV is a proud soldier of Bunker 8, responsible for defending the west border of his country. They were attacked by the enemy at night without any prior information and hence were hit hard. WAV immediately tried contacting Headquarters but his message got corrupted in between and now the Headquarters are unable to respond to their soldiers' message.

Help the Headquarters to decipher the message and help their men! The answer format is CTF{message}, the message exactly in the same format as obtained, no spaces.

## Relevant files / links

- [Message](./Message.wav/)
- [Google Drive link](https://drive.google.com/file/d/1YuBsLLDBuEQ5VxQtgCyFMj50d5a1ozIK/view?usp=sharing)

## Hint

1. The numbers involved in playing the file might require a little bit of magic...
2. Shall you succeed in recovering the file, try going about it pictorially...

## Solution

The problem primarily involves `Audio Steganography` and use of `File Signatures`. Steganography is a method of hiding secret data, by embedding it into some file, in this case, an audio file. It is one of the methods employed to protect secret or sensitive data from malicious attacks. File signatures (also known as File Magic Numbers) are bytes within a file used to identify the format of the file. They’re generally 2 - 4 bytes long and are found at the beginning of a file.

As the file is corrupted, we must first recover it. To be precise, the file signature of the audio file has been modified. The first few bytes contain information regarding the format as mentioned above, so on modifying those, the file is rendered useless. The name of the soldier `WAV` gives us the file format for the audio file. Using the first hint, one can look up the `Magic Number` of wav extension `52 49 46 46 RIFF`. We just need to replace the incorrect values with these using a `Hex Editor` and the audio file starts playing again.

The next step is to find the image that has been converted into an audio file. The second hint gives us the idea of hiding visual data in audio. This can be done using some online tools, the most popular being `Audacity`. They must load the image using the software and then play it in `Spectrogram` format, which is a visual way of representing the signal strength. The image will be visible containing the flag which is our final answer.

The image containing the flag, the original message and the corrupted message all have been uploaded. The softwares used to create the question are as follows:

- [Hex Editor](https://www.onlinehexeditor.com/#)
- [Caogula](https://www.abc.se/~re/Coagula/Coagula.html)
- [Audacity](https://www.audacityteam.org)
