import random
rast=random.randint(3,11)
Sayi=(3*rast)+1
print("Oyun Kuralları: Sadece 2 veya 1 düşebilirsiniz.")
print(Sayi)
while Sayi >=0:
    try:
        tahmin=int(input("Tahmininizi yapiniz:"))
        if Sayi-tahmin > 2 or Sayi-tahmin < 0 or tahmin==Sayi:
            print("Girdiğinz değer 2 veya 1 den daha fazla, az veya eşittir. Lütfen geçerli bir sayi giriniz...")
        else:
            if tahmin==0:
                print("Kaybettiniz. Ancak kazanamazsınız da :D")
                break
            if Sayi-tahmin==1:
                Sayi=tahmin
                Sayi=Sayi-2
                print(Sayi)
            if Sayi-tahmin==2:
                Sayi=tahmin
                Sayi=Sayi-1
                print(Sayi)
            if Sayi<=0:
                print("Tebrikler Kazandınız. Nasıl Kazandın LAN")
    except:
        print("Lütfen geçerli bir sayi girin.")