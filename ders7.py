sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))

ikisi_de_cift = (sayi1 % 2 == 0) and (sayi2 % 2 == 0)

print("Her iki sayı da çift mi?", ikisi_de_cift)
