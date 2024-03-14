SBOXSATIR = []
SBOX = []
SBOXES = []
import random
for j in range(8):
    for i in range(4):
        while(len(SBOXSATIR) < 16):
            uretilen = random.randint(0, 15)
            t = True
            for y in SBOXSATIR:
                if (uretilen == y):
                    t = False
            if (t):
                SBOXSATIR.append(uretilen)
        SBOX.append(SBOXSATIR)
        SBOXSATIR = []
    SBOXES.append(SBOX)
    SBOX = []
print(SBOXES[0][1][1])
print(SBOXES)