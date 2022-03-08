# Favorite Website

Author: Srujan Bharadwaj

Flag: `CTF{C@@kie$_@re_the_be$t}`

## Problem Statement

After a long time, Alex tries to visit his favorite website. But nobody thought he would become very unlucky. Visit the [website](https://wec-ctf-2022-web.herokuapp.com/q2)  and help him get the flag.

## Relevant files / links

- [Website link](https://wec-ctf-2022-web.herokuapp.com/q2)

## Hint

Do you know how websites track users?

## Solution

The first thing to think of is cookies. There is more than one cookie to make the task harder. But only one of the cookies track of the number of times the user visits. After experimenting with it and observing every cookie, it is clear that only the cookie named _gatj changes. The cookies are URL encoded. So, decode it using [URL Encode-Decode](https://www.url-encode-decode.com/). But they will still be in base64 encoded form. So, decode them using base64 decoders. The decoded string looks something like this ``still cannot solve this task?times=00000000&id=f08b5a1e-7635-45aa-aed7-3e2a3d9c3568``. 
``times`` parameter keeps track of the number of times a person refreshes the page. So use an extension to edit this cookie. Then encode it using a base64 encoder. After that encode it using URL encoders. Then refresh the page to get the flag.
