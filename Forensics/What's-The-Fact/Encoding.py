from PIL import Image
import numpy as np

img = Image.open(r"Original.jpg")

image_array = np.array(img, dtype = 'uint8')
image_array_original = np.array(img, dtype = 'uint8')

plaintext = "TheWorldIsaCruelPlace"
B64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
encodedtext = ""


for i in range(len(plaintext)):
    index = B64.find(plaintext[i])
    temp = bin(index).replace("0b", "")
    if(len(temp) < 6):
        n = len(temp)
        for i in range(6 - n):
            temp = '0' + temp
    
    encodedtext += temp


for i in range(len(encodedtext)):
    num = image_array[0][i][2]

    if encodedtext[i] == '1':
        if num % 2 == 1:
            continue
        else:
            num += 1

    else:
        if num % 2 == 0:
            continue
        else:
            num += 1

    image_array[0][i][2] = num

img = Image.fromarray(image_array)
img.save('Drake_Meme.png')