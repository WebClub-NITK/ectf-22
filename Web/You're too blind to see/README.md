# You're too blind to see

Author: Chinmaya Sharma

Flag: `CTF{W3r3_N0_57r4N63r5_70_10V3}`

## Problem Statement

Army pilot Stevens, recruited for a top-secret operation, finds himself in the body of an unknown man. 
He keeps finding himself in a 1990s music video and does not know how to get out. Help him find the flag that will help him get out of the loop.
## Relevant files / links

- [Website link](https://chinmayasharma-hue.github.io/CTF2022.gitbhub.io/)

## Hint

Help colter stevens find his way inside the simulation.

## Solution

One of the ways of hiding information in a website is in the page source. The page source has 
a gmail account username is the base64 encoded format, and when any mail is sent to this mail,
it gives the password to the site which redirects to another site containing the flag.
