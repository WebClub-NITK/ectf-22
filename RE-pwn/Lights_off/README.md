# Lost Password

Author: Asim Jawahir

Flag: `CTF{L1Ghts=O}`

## Problem Statement

Jett has forgotten her password for her bedroom lights. She isn't able to turn off the lights without  them. Help her to find out what is the password by reverse engineering the given algorithm. Login to the server to enter the password so jett can turn off the lights.

### How to access the server

#### For Linux-Based Systems
``` shell
sudo apt-get install netcat
nc 40.114.6.167 5555
```

## Relevant files / links

- [main.c](./main.c)


## Solution

After closely analyzing the code, we can understand that the code only accepts strings of length 4.

### Brute forcing the algorithm.
We can brute force a solution via the following code
``` c
    char arr[100];
    scanf("%s", &arr);
    int k = strlen(arr);
    a = 25;
    for (int i = 0; i < k / 2; i++)
    {
        printf("%d", (i % 2 ? arr[i] + a : arr[i] - a));
        printf(" %d\n", ((k - 1) % 2 ? arr[k - i - 1] + a : arr[k - i - 1] - a));
    }
```
We get the following code by printing the if statement conditions. 
Try to increment and decrement the characters present in the inputted string until we get the desired output.

### Analyzing the algorithm
After closly alayzing the if statment we can guess figure out the following conditions for the secret code to be true.
1. a[0] - a[3] = 50
2. a[1] == a[2]

Use the following command to access the server
```
nc 40.114.6.167 5555
```

type the password(an example of a password is: b550) and press enter

The following message will be displayed: `CTF{L1Ghts=O}`
