import base64
from PIL import Image
import numpy as np

img = Image.open(r"Drake_Meme.png")
image_array = np.array(img, dtype = 'uint8')

encoded_text = ""
for i in range(126):
    if image_array[0][i][2] % 2 == 0:
        encoded_text += '0'
    else:
        encoded_text += '1'

B64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
decoded_text = ""
i = 0

while i < 126:
    num = 0
    for j in range(6):
        if encoded_text[i + j] == '1':
            num += pow(2, 5 - j)

    i = i + 6
    decoded_text += B64[num]

print(decoded_text)
