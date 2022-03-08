# The invincible device

Author: Sudesh Gowda J

Flag: CTF{PLEASEBUYATOUCHPHONE}

## Problem Statement

Agent "Le chiffrage indéchiffrable" recieved an audio from an invincible device named "Kinoa". Help the agent decode the message.


Flag format: CTF{FLAGINCAPSWITHNOSPACES}

## Relevant files / links

- [chall.mp3](./chall.mp3)

## Hint


## Solution

Proposed difficulty level: Medium

When [chall.mp3](./chall.mp3) is opened in an audio editor like Audacity, it can be seen that it is a stereo track(this is also evident while listening). There are [DTMF tones](https://en.wikipedia.org/wiki/Dual-tone_multi-frequency_signaling) in both tracks. Splitting the tracks and then using some [online tool](http://dialabc.com/sound/detect/) to detect the tones will give <code>22 7 9 7777 7777 55 333 44 6 8 55 7777 9 55 555 55 555 777 9999 444</code> and <code>6 33 7777 7777 2 4 33 66 666 8 777 33 222 444 33 888 33 3</code>. 

Applying [Multi-tap cipher](https://www.dcode.fr/multitap-abc-cipher) on the obtained sequence of numbers will give <code>BPWSSKFHMTKSWKLKLRZI</code> and <code>MESSAGENOTRECIEVED</code>, respectively. The name "Le chiffrage indéchiffrable" leads us to [Vigenere cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher). We have two strings, using <code>MESSAGENOTRECIEVED</code> as the key for decrypting the ciphertext <code>BPWSSKFHMTKSWKLKLRZI</code> will provide the flag <code>PLEASEBUYATOUCHPHONE</code>.
