# What is this

Author: [Shashank D](https://github.com/shashank68)

Flag: `CTF{D0cker_ent3r5_the_p4rty}`

## Problem Statement

Intelligence has found some wierd material from Mr. Codeshankar(yes, it's him yet again). So it's your task now to find out what's contained in it. 

## Relevant files / links

- [Wierd material](https://drive.google.com/file/d/1fFAexozA987VAgDI2AnOcr4ei2TLUO6Q/view?usp=sharing)


## Solution

The given file is a zip compressed file containing a tar archive file. After extraction, we see many folders of layers with SHA hash names & manifest.json. This is the standard format of a docker image. This can be loaded using the docker cli tool.
```bash
docker load --input=<image.tar>
```

Now just spawning a container from the image will print out the flag.
