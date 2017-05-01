def highest(n):
    flag = False
    p = 1
    while flag == False:
        if (2**p) <= n:
            p += 1
        else:
            p -= 1
            flag = True
            return 2**p

def expand(k):
    bases = list()
    while k >= 1:
        base = highest(k)
        bases.append(base)
        k = k - base
    print("Expansion:", bases)
    return bases
    

def decodeM():
    while True:
        a, k, m = input("Enter the base (a), the exponent (k), and the mod (m), in the format a, k, m: ").strip().split(",")
        a = int(a)
        k = int(k)
        m = int(m)
        b = 1
        subset = list()
        subset = expand(k)

        for p in subset:
            b = b*(a**p)%m
            print(str(a) + "^" + str(p) + " is congruent to " +  str(b) + " mod (" + str(m) + ")")
        b = b%m
        print(b)

decodeM()


