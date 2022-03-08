import random
import time
import hashlib

t = round(time.time())
for i in reversed(range(t)):
    random.seed(i)
    x = random.random()

    if (x == 0.33567959567961436):
        print("****************  seed is "+ str(i)+ " ****************")
        
        random.seed(i , version=2)

        while True:
            rand = random.random()
            has = hashlib.sha256(str(rand).encode()).hexdigest()
            flag = f"CTF{{{has}}}"
            if "7a2" in has:
                with open("./flag", "w") as f:
                    f.write(flag)
                    print("Flag written to file")
                    exit(0)
