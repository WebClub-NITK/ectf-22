# Broken Pieces

Author: Kavya Bhat

Flag: `CTF{th@nk2_f0r_h3lping}`

## Problem Statement

Oh no! I broke this framed image. Unless you can magically put it together, I’m in big trouble. <br>
Flag format: CTF{...}

## Relevant files / links

- [pieces.zip](./pieces.zip)

## Solution

Unzipping the file `pieces.zip` presents a folder with 400 black-and-white jpg files (could it be a QR code?). These are labeled in the order `0101, 0102, ... 2020` which gives us a clue that it might be a matrix of some kind. Considering the phrase `broken pieces` and the idea of putting it together, a quick search reveals the [ImageMagick](https://imagemagick.org/script/command-line-options.php) tool, which allows you to work with images from the command line.<br> `magick montage` is one such command that has an option called `-tile`. This helps merge multiple images into a matrix of the required width and height. <br>
Using this command: `montage -tile 20x20 -geometry +0+0 qr.jpg` generates a merged image named [qr.jpg](./qr.jpg).

The option `-tile 20x20` merges the images such that it has a width and height of exactly 20 files each.<br>
The option `-geometry +0+0` ensures that no border is present between individual images.

The obtained image is a QR code, which on scanning reveals the text `th@nk2_f0r_h3lping`.<br>
The flag to this challenge would be `CTF{th@nk2_f0r_h3lping}`.                    
