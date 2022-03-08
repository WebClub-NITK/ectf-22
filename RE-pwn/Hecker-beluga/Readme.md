# Hecker Beluga

Author: Balajinaidu V

Flag: `CTF{r3verS!ng_pyTh0n}`

## Problem Statement

Skittle has a password validator but it is easily reversible. His friend Beluga noticed this, help beluga to show his hecker skills by getting the password.

Flag format: CTF{password}

## Relevant files / links

- [pass_validator.py](./pass_validator.py)


## Solution

### Step 1: Length of the password

```python
if(len(password[::-2]) != 8):
    print("Nah, you're not even close!!")
    return False
```
`password[::-2]` In python gives all the characters in the list from the end taking 2 steps at a time. To pass this check `len(password[::-2]) == 8)` so length of the password can be 16 (Does a 15 char password work 😉 ?).

### Step 2: Reversing chunk1

``` python
pwlen = len(password)
chunk1 = 'key'.join([chr(0x98 - ord(password[c])) for c in range(0, int(pwlen / 2))])
```
We see that it operates on the characters of the password from index 0 to `pwlen / 2`, where `pwlen` is the length of the password. We know the password is 16 characters long (atleast I knew😉), `pwlen/2 = 8`. The following operations are performed on first 8 characters.

1. Each character of the password into an integer using `ord`.
2. Subtracting each of these integers from `0x98`.
3. Converting the resultant back into a character using `chr`.
4. Constructing a string by putting the word “key” between each character returned.

```python
if "".join([c for c in chunk1[::4]]) != '&e"3&Ew*':
    print("Seems you're a terrible reverse engineer, come back after gaining some skills!")
    return False
```

Here, we use another string constructed from `chunk1` by taking every 4th character of chunk1, starting from the first one. This essentially removes `key` from `chunk1` string and compares the new string with `&e"3&Ew*`. Now to reverse this to get the first 8 characters of password subract `0x98` from the ordinal of each character of `&e"3&Ew*`(ie `chr(0x98-ord('&')) = 'r'`) this gives `r3verS!n`.

### Step 3: Reversing chunk2

```python
chunk2 = [ord(c) - 0x1F if ord(c) > 0x60 else (ord(c) + 0x1F if ord(c) > 0x40 else ord(c))
              for c in password[int(pwlen / 2) : int(2 * pwlen / 2)]]
rand = [54, -45, 9, 25, -42, -25, 31, -79]
for i in range(0, len(chunk2)):
    if(0 if i == len(chunk2) - 1 else chunk2[i + 1]) != chunk2[i] + rand[i]:
        print("You're not a real hecker, try again! " + str(i))
        return False
```

We see that the list comprehension being used to construct `chunk2` returns the result of some arithmetic operations on the ordinal value of each character (which is obtained using the `ord` function). So `chunk2` is a list of 8 integers. 

Then there is a list of random integers `rand` which is used to validate `chunk2`. Let’s go in reverse and figure out the integer array `chunk2`. 
Here is the condition (where `i` is the index):
```python
if(0 if i == len(chunk2) - 1 else chunk2[i + 1]) != chunk2[i] + rand[i]:
```

when i = 7 (`len(chunk2)-1`), the condition becomes `0 != chunk2[7] + rand[7]`, to get the password right we have to pass this check so `chunk2[7] + rand[7] = 0` rand[7] is -79, which makes `chunk2[7] = 79`. Now we know chunk2[7] using this we get all other values of chunk2(`chunk2[i] = chunk2[i+1] - ring[i]`).

```python
chunk2 = [72, 126, 81, 90, 115, 73, 48, 79]
```

Now from this we can figure out the characters by reversing the part that generates `chunk2`.
``` python
def inverse_chunk2_char(x):
  if x > 95:
    return chr(x - 0x1F)
  elif x > 65:
    return chr(x + 0x1F)
  else:
    return chr(x)

result = ''.join(list(map(inverse_chunk2_char, chunk2)))
# 'g_pyTh0n'
```
With that we get next 8 characters of the password.
<b>Flag: `CTF{r3verS!ng_pyTh0n}`</b>
