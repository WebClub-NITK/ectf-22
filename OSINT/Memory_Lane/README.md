# Memory Lane

Author: Kavya Bhat

Flag: `CTF{th3_g00d_0ld_t1mes}`

## Problem Statement

I miss way back when everything was simpler. Well, except for the time I almost gave away a secret on my YouTube channel. I was able to rectify it quickly, hopefully without anyone noticing…

## Relevant files / links 

- http://shorturl.at/grCQS

## Solution

The link provided leads you to a YouTube channel that has only one video. Nothing seems to be available at most sections, except the `About` section. <br>
The description has a flag `CTF{1s_th1s_wh@t_y0u_need}`, but it actually isn't what we need.<br>
 The problem statement hints at previous changes that were made to this channel. Looking closely, the phrase `way back` is a hint to the `WayBack Machine` which allows users to see how websites looked in the past. <br>

Entering the URL of the `About` section in the WayBack Machine reveals that there exists a capture of that webpage in the archives. <br>
The [archived webpage](./wayback.jpg) reveals the secret, `CTF{th3_g00d_0ld_t1mes}`.