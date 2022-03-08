# Hack the Auth

Author: Srujan Bharadwaj

Flag: `CTF{SHA256_AND_WEB}`

## Problem Statement

Alex's friend sent him a website that stores the data of many Billionaires. But he doesn't know the username and password to log in. Help him win the bounty prize by getting the credentials. [Website link](https://wec-ctf-2022-web.herokuapp.com/q1)

## Relevant files / links

- [Website link](https://wec-ctf-2022-web.herokuapp.com/q1)

## Hint

Something's happening within the browser after clicking login. May the source be with you.

## Solution

By going through the source code of the page, username can be found(admin). The password entered is encrypted using sha256 algorithm before sending to the server which can also be seen in the source code. Even the real password's hash can be found - dfbec338b51c5643ba481625e1075236d3a9a07fbd6393763f253e99024958a4
Since the password is not strong, the actual password can be found using  online tools like [Crackstation](https://crackstation.net/). Then login with the correct credentials. Once it is done, a cookie is set with the flag as cookie value. Decode the cookie which is in percent encoded format. Tools like [URL encode-decode](https://www.url-encode-decode.com/) can be used for that.
