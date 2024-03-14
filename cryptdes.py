# Burak BAKIRCI - DES
import constants as CT
# constants.INITIALPERMUTATIONTABLE : Başlangıç permütasyonu tablosu
# constants.FINALPERMUTATIONTABLE : Final permütasyonu tablosu
# constants.EBOX : Expansion Box Tablosu
# constants.PM56BIT : 56 bit seçici tablo
# constants.PM48BIT : 48 bit seçici tablo
# constants.PM32BIT : 32 bit permütasyon tablosu
# constants.sboxtanSonucGetir(0,1,2) : 1. Sbox, 2. satır 3. satırdaki sayıyı veriyor
def ikiParcayaBol(data):
    res = []
    sol = data[0:int(len(data) / 2)]
    sag = data[int(len(data) / 2): len(data)]
    res.append(sol)
    res.append(sag)
    return res
def trKarakter(ascii):
    # ı , İ , ş , Ş , ğ , Ğ için sırasıyla
    # 200,201,202,203,204,205 kullanılacak
    if (ascii == 305):
        return 200
    elif(ascii == 304):
        return 201
    elif(ascii) == 351:
        return 202
    elif(ascii) == 350:
        return 203
    elif(ascii) == 287:
        return 204
    elif(ascii) == 285:
        return 205
    else:
        return ascii
def trKarakterTersi(ascii):
    # ı , İ , ş , Ş , ğ , Ğ için sırasıyla
    # 200,201,202,203,204,205 kullanılacak
    # deşifrede gelen değer 200 ise aslında 305 gelmiştir.
    if (ascii == 200):
        return 305
    elif(ascii == 201):
        return 304
    elif(ascii) == 202:
        return 351
    elif(ascii) == 203:
        return 350
    elif(ascii) == 204:
        return 287
    elif(ascii) == 205:
        return 285
    else:
        return ascii
def decimalToBinary(decimal):
    decimal = trKarakter(decimal)    
    binary = ""
    while(decimal > 0):
        binary += str(decimal % 2)
        decimal = int(decimal / 2)
    res = ""
    for c in range(len(binary)-1,-1,-1):
        res += binary[c]
    if (len(res)<8):
        for d in range(8-len(res)):
            res = "0" + res 
    return res
def decimalToBinary4bit(decimal):   
    binary = ""
    while(decimal > 0):
        binary += str(decimal % 2)
        decimal = int(decimal / 2)
    res = ""
    for c in range(len(binary)-1,-1,-1):
        res += binary[c]
    if (len(res)<4):
        for d in range(4-len(res)):
            res = "0" + res 
    return res
def metinToBinary(metin):
    binary = ""
    for x in metin:
        binary += decimalToBinary(ord(x))
    return binary
def anahtar(key):
    if(len(key) > 8):
        key = key[0:7]
    if (len(key) < 8):
        for d in range(8-len(key)):
            key = "a" + key
    return metinToBinary(key)
def initialPermutation(data):
    d = []
    res = ""
    for j in range(64):
        d.append("#")
    for i in range(64):
        d[CT.INITIALPERMUTATIONTABLE[i]-1] = data[i]
    for k in d:
        res = res + k
    return res 
def finalPermutation(data):
    d = []
    res = ""
    for j in range(64):
        d.append("#")
    for i in range(64):
        d[CT.FINALPERMUTATIONTABLE[i]-1] = data[i]
    for k in d:
        res = res + k
    return res
def produceKeys(data):
    key64bit = anahtar(data)
    key56bit = keyPermutationFor56Bit(key64bit)
    print(key56bit)
    ikiParcaKey = ikiParcayaBol(key56bit)
    solKey = ikiParcaKey[0]
    print("sol " + solKey)
    sagKey = ikiParcaKey[1]
    print("sağ " + sagKey)
    KEYS = []
    for x in range(16):
        solKey = solaKaydır(solKey, CT.ROUNDS[x])
        sagKey = solaKaydır(sagKey, CT.ROUNDS[x])
        finalKey = keyPermutationFor48Bit(solKey + sagKey)
        KEYS.append(finalKey)
    return KEYS
def keyPermutationFor56Bit(key):
    print(key)
    d = []
    res = ""
    for i in range(56):
        d.append(key[CT.PM56BIT[i] -1])
    for k in d:
        res = res + str(k)
    return res   
def keyPermutationFor48Bit(key):
    d = []
    res = ""
    for i in range(48):
        d.append(key[CT.PM48BIT[i]-1])
    for k in d:
        res = res + str(k)
    return res     
def solaKaydır(bits, sayı):
    kaydırma = bits[0:sayı]
    bits = bits + kaydırma
    bits = bits[len(kaydırma): len(bits)]
    return bits
def expansionBox(m):
    tmp = [0] * 48
    res = ""
    for j in range(48):
        tmp[j] = m[CT.EBOX[j]-1]
    for i in tmp:
        res = res + i
    return res
def mesaji64bitGrupla(m):
    uzunluk = len(m)
    mesajGrubu = []
    for i in range(0, uzunluk, 64):
        parca = m[i:i+64]
        if (len(parca) == 64):
            mesajGrubu.append(parca)
        elif(len(parca) > 0):
            for j in range(64-len(parca)):
                parca = parca + "0" 
            mesajGrubu.append(parca)
    return mesajGrubu
def sBoxPermutation(m):
    d = []
    res = ""
    for j in range(32):
        d.append("#")
    for i in range(32):
        d[CT.PM32BIT[i]-1] = m[i]
    for k in d:
        res = res + k
    return res 
def dataSbox(data):
    inputlar = []
    for i in range(0,48,6):
        inputlar.append(data[i:i+6])
    sBoxNo = 0
    res = ""
    for x in inputlar:
        row = int((x[0] + x[5]),2)
        column = int(x[1:4], 2)
        res = res + decimalToBinary4bit(CT.sboxtanSonucGetir(sBoxNo, row, column))
        sBoxNo += 1
    return res
def dataXor(a,b):
    res = ""
    for i in range(len(a)):
        res = res + str(int(a[i],2)^int(b[i],2))
    return res
def dataExpansionXorAnahtar(data, anahtar):
    res = ""
    if (len(data) != 32):
        print("Data uyumsuzluğu var")
    else:
        data = expansionBox(data)
        for i in range(48):
           res = res + str(int(data[i],2)^int(anahtar[i],2)) 
    return res
def DES(data, type):
    data = initialPermutation(data)
    data32Bits = ikiParcayaBol(data)
    L = data32Bits[0]
    R = data32Bits[1]
    Ryedek = R
    if (type == 0):
        for x in range(16):
            R = dataExpansionXorAnahtar(R,KEYS[x])
            R = dataSbox(R)
            R = sBoxPermutation(R)
            R = dataXor(L,R)
            L = Ryedek
            Ryedek = R
    else:
        for x in range(15,-1,-1):
            R = dataExpansionXorAnahtar(R,KEYS[x])
            R = dataSbox(R)
            R = sBoxPermutation(R)
            R = dataXor(L,R)
            L = Ryedek
            Ryedek = R
    cipher = finalPermutation(R + L)
    return cipher
def binaryToHex(binary):
    return hex(int(binary, 2))
def binaryToMetin(hex):
    data = str(hex)
    res = ""
    for x in range(0, len(data), 8):
        res = res + chr(trKarakterTersi(int(data[x:x+8], 2)))
    return res
mesaj = input("Şifrelenecek metni yazın : ")
KEYS = produceKeys(input("Şifreleme anahtarını yazın : "))
crypted = ""
decrypted = ""
binaryMesaj = metinToBinary(mesaj)
mesaj64bitGruplar = mesaji64bitGrupla(binaryMesaj)
for d in mesaj64bitGruplar:
    crypted = crypted + DES(d, 0)
crypted64bitGruplar = mesaji64bitGrupla(crypted)
for e in crypted64bitGruplar:
    decrypted = decrypted + DES(e, 1)
print("Şifrelenecek metin : " + mesaj)
print("Metin hex kodu     : " + binaryToHex(metinToBinary(mesaj)))
print("Şifreli metin hex  : " + binaryToHex(crypted))
print("deşifre metin hex  : " + binaryToHex(decrypted))
print("deşifre metin      : " + binaryToMetin(decrypted))