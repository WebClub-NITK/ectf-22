# Vacation

Author: Kavya Bhat

Flag: `CTF{f0und_th3_fl@g}`

## Problem Statement

People even try to turn their pets into celebrities, it gets annoying quite fast. That reminds me, have you come across @tig3r_and_b3ar ? Apparently their owner is a photographer, I haven’t contacted her though.

## Hint

Have you tried contacting her?

## Solution

Considering their owner is a photographer, the ideal place to search for the given handle would be on Instagram. Searching on the site with the exact handle gives us a profile made for 2 pets. 
This profile has only 1 follower, with the handle @ashlynbardot - presumably the owner. This seems right, since the bio of the profile (@ashlynbardot) mentions 'Photographer'. There's also an email address provided, `ashlynbardot@yahoo.com`. 

There is no other way of contacting this person, so we can send an email to the given address. We get an [autoresponse](./response.jpg) a few moments later, containing the flag `CTF{f0und_th3_fl@g}`.

