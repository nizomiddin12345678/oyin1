import  random
def Irand():
        return random.choice(["share", "steal"])

def Cash_machine():
    odam1 = 3
    odam2 = 3
    result = []
    Max = 4
    count = 0

    while count < Max:

        count += 1
        a1 = Irand()
        a2 = Irand()
        if a1 == "share":
            odam1 -= 1
            odam2 += 2

        elif a1 =="steal":
            odam1 += 3

        if a2 == "share":
            odam2 -= 1
            odam1 += 2

        elif a2 == "steal":
            odam2 += 3
        result.append([odam1,odam2])

        print(f"{count}: Odam 1: {a1}  ,Odam 2: {a2} => Tangalar: {result[-1]}")
    print("- - - N A T I J A - - -")
    if odam1 >odam2:
        print("1- Yutdi!","1 da",odam1,"achko","2 da ",odam2,"achko")
    elif odam2 == odam1:
        print("Durang",odam1 ,"=", odam2)
    else:print("2- Yutdi!","2 da",odam2,"achko","1 da ",odam1,"achko")


Cash_machine()

