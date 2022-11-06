def szorzas():
    elrendezes = "{0:>4}{1:>4}{2:>4}{3:>4}{4:>4}{5:>4}{6:>4}{7:>4}{8:>4}{9:>4}{10:>4}{11:>4}"
    ures = "   "

    print(ures,elrendezes.format("1","2","3","4","5","6","7","8","9","10","11","12"))
    print(" :--------------------------------------------------")

    teli = ""
    for i in range(1,13):
        ures = str(i)
        teli = ures+":"
        teli2 = ures+": "
        if i < 10:
            print(teli2,elrendezes.format(i,i*2,i*3,i*4,i*5,i*6,i*7,i*8,i*9,i*10,i*11,i*12))
        else:
            print(teli,elrendezes.format(i,i*2,i*3,i*4,i*5,i*6,i*7,i*8,i*9,i*10,i*11,i*12))


def palidrom():
    BeKer = input("kérem a szavat:")
    BeK = BeKer.lower()
    VisszaF = ""
    teszt = ""
    ures1 = ""
    ures2 = ""

    for i in BeK:
        VisszaF = i + VisszaF
        for x in range(len(BeK)):
            ures1 = BeK[x]
            ures2 = BeKer[x-1]
            if ures1 + ures2 == "zs":
                print(":(")
                break



    if (BeK == VisszaF):
        print(f"Igen, {BeK} egy palindróm szó!")
    else:
        print(f"{BeK} nem számít palindróm szónak!")

if __name__=="__main__":
    szorzas()
    palidrom()