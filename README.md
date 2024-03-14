# Data Encryption Standart Python(Pure) - Türkçe(Turkish) - Kütüphanesiz(No Library)

Sabitler
Yardımcı Fonksiyonlar
Ana Program ve Fonksiyonlar

# 1- Sabitler (constants.py)

INITIALPERMUTATIONTABLE : Başlangıç permütasyonu tablosu verinin 64 bit halinde parçalara bölünmesinden sonra ilk olarak bitlerinin yer değiştirileceği tablodur. Yani bu tablodaki ilk sayı verinin o sayıdaki bitinin yeni oluşturulacak 64 bit verideki ilk bit olarak yer değiştirilmesi olarak tanımlanabilir. 

FINALPERMUTATIONTABLE   : Final permütasyon tablosu 64 bit verinin şifreleme işlemi yapıldıktan sonra initial permütasyonda olduğu şekliyle son yer değiştirme işlemlerinin yapılmasıdır. 

EBOX : Expansion box da 32 bit veri tekrarlı permütasyon tablosu ile 48 bite çıkarılması için kullanılan dizidir.


ROUNDS : 56 bit Anahtarın 28 er bit sol ve sağ olarak 2’ye bölündükten sonra kaç kez sola kaydırılması işlemini tutan veridir.


PM56BIT : 64 bit verinin 56 bitinin seçildiği dizidir


PM48BIT : 56 bit verinin 32 bitinin secildigi dizidir.


PM32BIT : SBOX tan çıkan 32 bit verinin bitlerinin yer değiştirme işlemi için kullanılan dizidir.


SBOXES : 48 bit gelen veri  bu tablolardan 32 bit olarak çıkar.

Açıklama  : DES standardında INITIALPERMUTATIONTABLE ile FINALPERMUTATIONTABLE değiştirilemez. Değiştirildiğinde deşifreleme işlemi yapılamaz. Diğer bütün sabitlerde ki değişiklikler DES’in çalışmasını etkilemez. En ufak bir değişiklik şifrelenmiş metinde değişikliğe yol açar.

# 2- Yardımcı Fonksiyonlar (ascii.py , sboxuretme.py)

ascii.py : Bu dosyada 0 dan 255 ya kadar olan sayıların karakter karşılıklarını göstermeye yarayan bir döngü kullanıldı.

sboxuretme.py : Bu dosyada rastgele sayılar ürettirilerek 8 adet SBOX dizisi oluşturulması sağlandı.

# 3- Ana Program ve Fonksiyonlar (cryptdes.py)

def ikiParcayaBol(data): Gelen veriyi sol ve sağ olmak üzere tam ortadan ikiye böler. 

def trKarakter(ascii): 6 adet türkçe karakterin sayısal karşılığı 0-255 arasında olmadığı için şifrelenecek metinde bu karakterler yerine kullanılmayan sayı karşılıkları geri döndürülüyor.

def trKarakterTersi(ascii):trkarekter fonksiyonunda yapılan işlemin tersidir.

def decimalToBinary(decimal): Gelen sayıyı 8 bitler halinde binary formatına çevirip geri döndürür.

def decimalToBinary4bit(decimal):Gelen sayıyı 4 bitler halinde binary formatına çevirip geri döndürür.

def metinToBinary(metin): Verilen metni ikilik sayı formatına dönüştürerek geri döndürür.

def anahtar(key): anahtar olarak verilen yazıyı 64 bit olacak şekilde ayarlayıp geri döndürür.
 
def initialPermutation(data): 64 bit olarak verilen veri initial permütasyon tablosundaki dizilim ile geri döndürülür.

def finalPermutation(data): 64 bit olarak verilen veri final permütasyon tablosundaki dizilim ile geri döndürülür.

def produceKeys(data): Anahtar olarak verilen metinden 16 adet anahtar oluşturup geriye 16 değerli bir dizi döndürür.

def keyPermutationFor56Bit(key) : 64 bit gelen anahtardan 56 bit seçilir.

def keyPermutationFor48Bit(key): 56 bit gelen anahtardan 48 bit seçilir.

def solaKaydır(bits, sayı): 28 bit olarak gelen veri(bits) ROUNDS tablosundan gelen sola kaydırma değeri(sayı) ile sola saydırılarak veri döndürülür

def expansionBox(m): 32 bit gelen veri 48 bite Expansion yapılır.

def mesaji64bitGrupla(m): Şifrelenecek olan metin 64’er bit olarak gruplanır ve bu 64 bit veriler bir dizi olarak geri döndürülür

def sBoxPermutation(m): PM32BIT tablosundaki yer değiştirme işlemi yapılır.
def dataSbox(data): 48 bit gelen veri sbox lara girer ve geriye 32 bit olarak çıkar.

def dataXor(a,b):a ile b verisini XOR yaparak geri dönderir.

def dataExpansionXorAnahtar(data, anahtar): Data olarak gelen veri öncelikle EBOX tablosuna girerek ve 32 bit ten 48 bit e yükseltilir.Sonra bu 48 bit veri mevcut (anahtar) ile XOR lanır ve geri döndürülür.

def DES(data, type): Şifreleme veya deşifreleme işlemlerinin yapıldığı fonksiyondur.type 0 ise şifreleme 1 ise deşifreleme işlemi yapılıyor.

def binaryToHex(binary): Binary veriyi HEX veriye çeviriyor.

def binaryToMetin(hex): Gelen HEX veriyi metin haline çevirir.

# İstemci Kodu :

```python
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
```