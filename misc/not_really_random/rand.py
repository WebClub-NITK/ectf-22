import random 
import time 
import hashlib

seed = round(time.time())

random.seed(seed, version=2)

while True:
    rand = random.random()
    has = hashlib.sha256(str(rand).encode()).hexdigest()
    flag = f"CTF{{{has}}}"
    if "7a2" in has:
        with open("./flag", "w") as f:
            f.write(flag)
            break
    else:
        print(f"Bad random value: {rand}")

print("Flag created 🎉")
