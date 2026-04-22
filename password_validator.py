while True:
    sifre = input("bir şifre giriniz:")
    sifre_uzunluk=False
    sifre_buyuk_harf=False
    sifre_kucuk_harf=False
    sifre_rakam=False 
    sifre_ozel_karakter=False
    if len(sifre) >= 8:
        sifre_uzunluk=True
    for harf in sifre:
        if harf.isdigit():
                sifre_rakam=True
        elif harf.islower():
                sifre_kucuk_harf=True
        elif harf.isupper():
                sifre_buyuk_harf=True
        elif not harf.isalnum():
                sifre_ozel_karakter=True
    if sifre_uzunluk and sifre_rakam and sifre_buyuk_harf and sifre_kucuk_harf and sifre_ozel_karakter :
        print("şifreniz gayet iyi ve güvenli")
        break
    else:
        if not sifre_uzunluk:
            print("şifreniz 8 karakterden büyük olmalıdır.")
        if not sifre_buyuk_harf:
            print("şifreniz büyük harf içermelidir.")
        if not sifre_kucuk_harf:
            print("şifreniz küçük harf içermelidir.")
        if not sifre_rakam:
            print("şifrenizde rakam içermiyor.")
        if not sifre_ozel_karakter:
            print("sifreniz özel karakter içermiyior. ")
        print("şifreniz daha güvenli olması amaçlı tekrar giriniz.")
