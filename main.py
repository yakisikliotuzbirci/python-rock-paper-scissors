import random

def hamleiste():
    while True:
        hamle = input("Hamle giriniz (taş/kağıt/makas) : ")
        if hamle in ["taş", "kağıt", "makas"]:
            return hamle
        else:
            print("Lütfen geçerli bir hamle giriniz")

def rakiphamleiste():
    hamleler = ["taş","kağıt","makas"]
    return random.choice(hamleler)

def kazananibelirle(hamle, rakiphamle):
    if hamle == rakiphamle:
        return "berabere"
    elif hamle == "taş":
        return "kazandınız" if rakiphamle == "makas" else "kaybettiniz"
    elif hamle == "kağıt":
        return "kazandınız" if rakiphamle == "taş" else "kaybettiniz"
    elif hamle == "makas":
        return "kazandınız" if rakiphamle == "kağıt" else "kaybettiniz"

def tekraroyna():
        return input("Tekrar oynamak istermisin (evet/hayır) : ") == "evet"

def oyunsonucuiste(tur, kazanilantur):
    print("########## SONUÇ ##########")
    print(f"Kazanilan tur sayısı : {kazanilantur}")
    if kazanilantur<tur//2:
        print("Sonuç : kaybettiniz")
    else:
        print("Sonuç : kazandınız")


def main():
    while True:
        try:
            tur = int(input("Kaç tur oynamak istersiniz : "))
        except ValueError:
            print("Girilen değer bir sayı değil")
        kalantur = tur
        kazanilantur = 0

        while kalantur > 0:
            kalantur = kalantur - 1
            print(f"########## TUR {tur-kalantur} ##########")

            hamle = hamleiste()
            rakiphamle = rakiphamleiste()

            print(f"Rakibinin hamlesi: {rakiphamle}")

            sonuc = kazananibelirle(hamle, rakiphamle)
            print(sonuc)

            if sonuc == "kazandınız":
                kazanilantur = kazanilantur + 1

        oyunsonucuiste(tur,kazanilantur)

        if not tekraroyna():
            break

if __name__ == "__main__":
    main()