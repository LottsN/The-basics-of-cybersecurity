q=1357
g=10

a=0
b=0

for i in range(1000):
    if pow(g,i)%q == 419:
        a = i
        print("a:", a)

        for k in range(1000):
            if pow(g,k)%q == 34:
                b = k
                print("b :", b)

                if pow(g, a*b) % q == 33:
                    print(True)