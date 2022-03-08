# What's in this?

Author: [Shashank D](https://github.com/shashank68)

Flag: `CTF{1t5_all_1n_l4yers}`

## Problem Statement

Intelligence has found some wierd material from Mr. Codeshankar(yes, it's him yet again. Sorry, running out of names). Well, Codeshankar isn't giving away the secret so easily this time. 

## Relevant files / links

- [Wierd material](https://drive.google.com/file/d/1I-DVkxxdd9hBNQWptCR4Tr_Ju-k_AwoS/view?usp=sharing)


## Solution

The given file is a tar archive. After extraction, we see many folders of layers with SHA hash names & manifest.json. This is the standard format of a docker image (as introduced in whatisthis challenge). This image file has to be loaded as an image.

This time though, the flag has been hidden in a different layer & the content of the file has been deleted in subsequent layers. 

Using tools like [dive](https://github.com/wagoodman/dive) that do docker layer inspection, we can find that the 2nd layer copies a file `a.txt` to `/usr/lib` directory. On extracting the `layer.tar` of that particular layer, we find the file with the flag.
