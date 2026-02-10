giriş = """
(1) Topla
(2) Çıkar
(3) Çarp
(4) Böl
(5) Karesini Hesapla
(6) Karekökünü Hesapla
(7) Yüzdelik Hesapla
(8) Genel Toplam
(c) Hafızayı Sıfırla
(q) Çıkış
"""
hafıza = []

print(giriş)
while True:
    soru = input("Yapmak istediğiniz işlemin numarasını girin")
    if soru == "q":
        print("çıkış")
        break
    elif soru == "1":
        girdi1 = input("Toplama işlemi için ilk sayıyı girin: ")
        if girdi1 == "ans":
            sayı1 = hafıza[-1]
        else:
            sayı1 = int(girdi1)
        girdi2 = input("Toplama işlemi için ikinci sayıyı girin: ")
        if girdi2 == "ans":
            sayı2 = hafıza[-1]
        else:
            sayı2 = int(girdi2)
        print(sayı1, "+", sayı2, "=", sayı1 + sayı2)
        hafıza.append(sayı1 + sayı2)
    elif soru == "2":
        girdi3 = input("Çıkarma işlemi için ilk sayıyı girin: ")
        if girdi3 == "ans":
            sayı3 = hafıza[-1]
        else:
            sayı3 = int(girdi3)
        girdi4 = input("Çıkarma işlemi için ikinci sayıyı girin: ")
        if girdi4 == "ans":
            sayı4 = hafıza[-1]
        else:
            sayı4 = int(girdi4)
        print(sayı3, "-", sayı4, "=", sayı3 - sayı4)
        hafıza.append(sayı3 - sayı4)
    elif soru == "3":
        girdi5 = input("Çarpma işlemi için ilk sayıyı girin: ")
        if girdi5 == "ans":
            sayı5 = hafıza[-1]
        else:
            sayı5 = int(girdi5)
        girdi6 = input("Çarpma işlemi için ikinci sayıyı girin: ")
        if girdi6 == "ans":
            sayı6 = hafıza[-1]
        else:
            sayı6 = int(girdi6)
        print(sayı5, "x", sayı6, "=", sayı5 * sayı6)
        hafıza.append(sayı5 * sayı6)
    elif soru == "4":
        girdi7 = input("Bölme işlemi için ilk sayıyı girin: ")
        if girdi7 == "ans":
            sayı7 = hafıza[-1]
        else:
            sayı7 = int(girdi7)
        girdi8 = input("Bölme işlemi için ikinci sayıyı girin: ")
        if girdi8 == 0:
            print("Hata! Bir sayı 0'a bölünemez.")
            continue
        else:
            if girdi8 == "ans":
                sayı8 = hafıza[-1]
            else:
                sayı8 = int(girdi8)
        print(sayı7, "/", sayı8, "=", sayı7 / sayı8)
        hafıza.append(sayı7 / sayı8)
    elif soru == "5":
        girdi9 = input("Karesini hesaplamak istediğiniz sayıyı girin: ")
        if girdi9 == "ans":
            sayı9 = hafıza[-1]
        else:
            sayı9 = int(girdi9)
        print(sayı9, "Sayısının karesi=", sayı9 ** 2)
        hafıza.append(sayı9 ** 2)
    elif soru == "6":
        girdi10 = input("Karekökünü hesaplamak istediğiniz sayıyı girin: ")
        if girdi10 == "ans":
            sayı10 = hafıza[-1]
        else:
            sayı10 = int(girdi10)
        if sayı10 < 0:
            print("Hata! Negatif sayıların karekökü hesaplanamaz.")
        else:
            print(sayı10, "Sayısının karekökü=", sayı10 ** 0.5)
        hafıza.append(sayı10 ** 0.5)
    elif soru == "7":
        girdi11 = input("Yüzdeliği alınacak sayıyı girin: ")
        if girdi11 == "ans":
            sayı11 = hafıza[-1]
        else:
            sayı11 = int(girdi11)
        girdi12 = input("Yüzdeliğin değerini girin: ")
        if girdi12 == "ans":
            sayı12 = hafıza[-1]
        else:
            sayı12 = int(girdi12)
        print(sayı11, "sayısının %", sayı12, "kadarı", sayı11 * sayı12 / 100)
        hafıza.append(sayı11 * sayı12 / 100)
    elif soru == "8":
        if len(hafıza) == 0:
            print("Hafıza henüz boş, hesaplanmış bir sonuç yok.")
        else:
            toplam = sum(hafıza)
            print("Genel Toplam=", toplam)
    elif soru == "c":
        hafıza.clear()
        print("Hafıza sıfırlandı.")
    else:
        print("Hata! Böyle bir işlem yok.")