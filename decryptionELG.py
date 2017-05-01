from random import randint
#ElGamal Cryptosystem
class Decryptor:

    def __init__(self):
        self.message = list()
        self.output = ""
        self.decoded = list()
        self.k = 278374
        self.p = 380803
        self.b = 2

        while True:
            self.getMessage()
            print()
            self.decision()
            self.output = ""
            self.decoded = list()
            print()

    def getMessage(self):
        self.message = (input("Enter a message: ")).upper()
            
    def getK(self):
        self.k = input("Enter the secret key (k): ")
        try:
            self.k = int(self.k)
        except:
            print("Invalid, the value must be an integer.")
            return self.getK()
        
    def decision(self):
        temp = input("Encode or decode message?: ").lower()
        if temp == "encode":
            self.encode()
        elif temp == "decode":
            self.decode()
        else:
            print("Sorry, your option wasn't recognized...")
            return self.decision()

    def getPB(self):
        self.p = input("Enter prime value (p): ")
        self.b = input("Enter base value (b): ")
        try:
            self.p = int(self.p)
            self.b = int(self.b)
        except:
            print("Invalid, the values must be integers.")
            return self.getPB()
    
    def encode(self):
        temp = list(self.message.upper())
        for e in range(0, len(temp), 3):
            m = ""
            r = randint(100,10000)
            a = self.successiveSquare(self.b, self.k, self.p)
            count = 0
            for i in range(0,3):
                if count + e >= len(temp):
                    pass
                else:
                    m += str(ord(temp[e + count])-64+10)
                count += 1
            e1 = self.successiveSquare(self.b, r, self.p)
            x = int(m) * a**r
            e2 = self.successiveSquare(x, 1, self.p)
            print(e1, e2)
    
    def decode(self):
        self.message = self.message.strip().split(",")
        temp = ""
        for e in range(0, len(self.message), 2):
            c = self.successiveSquare(int(self.message[e]), self.k, self.p)
            print("c =", c)
            u = self.modinv(c,self.p)
            print("u =", u)
            v = pow(u*int(self.message[e+1]), 1, self.p)
            print("v =", v)
            temp += str(v)
            print()
        for i in range(0, len(temp), 2):
            self.decoded.append(temp[i:i+2])
        print(self.decoded)
        self.decodeMessage()
        
    def successiveSquare(self, a, k, m):
        a = int(a)
        k = int(k)
        m = int(m)
        b = 1
        subset = list()
        subset = self.expand(k)

        for p in subset:
            b = b*(a**p)%m
        return b%m

    def expand(self, k):
        bases = list()
        while k >= 1:
            base = self.highest(k)
            bases.append(base)
            k = k - base
        return bases
    
    def highest(self, n):
        flag = False
        p = 1
        while flag == False:
            if (2**p) <= n:
                p += 1
            else:
                p -= 1
                flag = True
                return 2**p
            
    def modinv(self, a, m):
        g, x, y = self.extendGcd(a, m)
        if g != 1:
                raise ValueError
        return x % m
    
    def extendGcd(self, aa, bb):
        lastremainder, remainder = abs(aa), abs(bb)
        x, lastx, y, lasty = 0, 1, 1, 0
        while remainder:
            lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
            x, lastx = lastx - quotient*x, x
            y, lasty = lasty - quotient*y, y
        return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

    def decodeMessage(self):
        for c in self.decoded:
            c = int(c)
            c += 54
            self.output += chr(c)
        print(self.output)
            
Decryptor()
