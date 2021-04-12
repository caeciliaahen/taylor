import numpy as np
def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)

print("[Pilih bentuk persamaan]")
print(" [1] f(x) = ax^n + bx^(n-1) + ... + c")
print(" [2] f(x) = ln x")
na = 0
while na==0:
    pilih = int(input("Masukkan pilihan: "))

    if pilih == 1:
        na = 1
        fx = list(map(float, input("\nMasukkan variabel persamaan: ").split(',')))
        a = float(input("Masukkan nilai a: "))
        x = float(input("Masukkan nilai x: "))
        suku = int(input("Masukkan batas suku: "))

        if suku > 0:
            pangkat = len(fx)
            f = [[0 for fx in range(pangkat)] for y in range(suku)]
            k = -1
            for i in range(suku):
                for j in range(pangkat):
                    if i == 0:
                        f[0][j] = fx[j]
                    else:
                        if j >= 0:
                            f[i][j] = f[i - 1][j] * (j - k)
                        else:
                            f[i][j] = 0
                k += 1

            print("\n[Persamaan]\nf(x) =", end=' ')
            for i in reversed(range(pangkat)):
                if i == (pangkat - 1):
                    if f[0][i] != 0:
                        print(str(f[0][i]) + "x^" + str(i), end=' ')
                elif i == 1:
                    if (f[0][i] > 0):
                        print("+", str(f[0][i]) + "x", end=' ')
                    elif (f[0][i] < 0):
                        print(str(f[0][i]) + "x", end=' ')
                elif i == 0:
                    if (f[0][i] > 0):
                        print("+", str(f[0][i]) + " untuk a=" + str(a))
                    elif (f[0][i] < 0):
                        print(str(f[0][i]) + " untuk a=" + str(a))
                else:
                    if (f[0][i] > 0):
                        print("+", str(f[0][i]) + "x^" + str(i), end=' ')
                    elif (f[0][i] < 0):
                        print(str(f[0][i]) + "x^" + str(i), end=' ')

            k = -1
            for i in range(suku):
                for j in range(pangkat):
                    if j >= 0:
                        f[i][j] = f[i][j] * (a ** (j - k - 1))
                    else:
                        f[i][j] = f[i][j]
                k += 1

            sumf = [sum(row) for row in f]

        else:
            print("Jumlah suku minimal 1!")

    elif pilih == 2:
        na = 2
        a = float(input("\nMasukkan nilai a: "))
        x = float(input("Masukkan nilai x: "))
        suku = int(input("Masukkan batas suku: "))

        if suku > 0:
            print("\n[Persamaan]\nf(x) = ln x untuk a =", a)
            k = -1
            sumf = []
            for i in range(suku):
                if i == 0:
                    sumf.append(np.log(a))
                elif i == 1:
                    sumf.append(1 / a)
                else:
                    sumf.append(sumf[i - 1] * (-i + 1) / a)
                k += 1

            k = -1
            for i in range(suku):
                if i >= 0:
                    sumf[i] = sumf[i] * (a ** (-(i - k - 1)))
                else:
                    sumf[i] = sumf[i]
                k += 1

        else:
            print("Jumlah suku minimal 1!")

    else:
        print("[!] Silakan masukkan pilihan yang sesuai.")

print("\n[Deret Taylor]\nf(x) =", end=' ')
for i in range(suku):
    if i == 0:
        print(sumf[i], end=' ')
    elif i == 1:
        print("+ (" + str(sumf[i]) + "*(x-" + str(a) + "))/" + str(i) + "!", end=' ')
    else:
        print("+ (" + str(sumf[i]) + "*(x-" + str(a) + ")^" + str(i) + ")/" + str(i) + "!", end=' ')
print("+ ...")
print("f(" + str(x) + ") =", end=' ')
for i in range(suku):
    if i == 0:
        print(sumf[i], end=' ')
    elif i == 1:
        print("+ (" + str(sumf[i]) + "*(" + str(x) + "-" + str(a) + "))/" + str(i) + "!", end=' ')
    else:
        print("+ (" + str(sumf[i]) + "*(" + str(x) + "-" + str(a) + ")^" + str(i) + ")/" + str(i) + "!",
              end=' ')
print("+ ...")

taylor = []
for i in range(suku):
    taylor.append(sumf[i] * (x - a) ** i / factorial(i))

print("f(" + str(x) + ") =", end=' ')
for i in range(suku):
    if i == 0:
        print(taylor[i], end=' ')
    else:
        if taylor[i] >= 0:
            print("+", taylor[i], end=' ')
        else:
            print(taylor[i], end=' ')
print("+ ...")

sumtaylor = sum(taylor)

if (pilih==1 and suku >= pangkat):
    print("f(" + str(x) + ") =", sumtaylor)
else:
    print("f(" + str(x) + ") ≈", sumtaylor)