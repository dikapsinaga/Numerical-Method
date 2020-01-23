fx = lambda x: x ** 4 - 2 * (x ** 2) + x - 3
a = float(input("Masukkan a: "))
b = float(input("Masukkan b: "))
er = 1000
c = a
n = 0

if (fx(a) * fx(b) < 0):
    if (abs(fx(a)) < abs(fx(b))):
        a, b = b, a
    cek = True
    d = 0;
    s = 0
    print("%-9s\t%-12s\t%-12s\t%-12s\t%-12s\t%-12s\t%-12s" % ("iterasi", "a", "b", "c", "s", "d", "Er (%)"))

    while (er > 0.0001):

        # Rumus inverse quadratic interpolation
        if (fx(a) != fx(c) and fx(b) != fx(c)):
            s = (a * fx(b) * fx(c) / ((fx(a) - fx(b)) * (fx(a) - fx(c)))) + (b * fx(a) * fx(c) / ((fx(b) - fx(a)) * (fx(b) - fx(c)))) + (c * fx(a) * fx(b) / ((fx(c) - fx(a)) * (fx(c) - fx(b))))

        # Rumus Secant
        else:
            s = b - ((fx(b) * (b - a)) / (fx(b) - fx(a)))

        # ceck kondisi
        if ((s < ((3 * a) + b) * 0.25) or (s > b)) or (cek and (abs(s - b) >= (abs(b - c) * 0.5))) or (not cek and (abs(s - b) >= (abs(c - d) * 0.5))) or (cek and (abs(b - c) < 0.1)) or (not cek and (abs(c - d) < 0.1)):

            # rumusb biseksi
            s = (a + b) / 2

            cek = True
        else:
            cek = False
        er = abs((s - a) / s)
        d = c; c = b
        if (fx(a) * fx(s) < 0):
            b = s
        else:
            a = s
        if (abs(fx(a)) < abs(fx(b))):
            a, b = b, a
        print("%-9d\t%-12f\t%-12f\t%-12f\t%-12f\t%-12f\t%-12f" % (n, a, b, c, s, d, er))
        n += 1
    print("Akar persamaan adalah %f" % (s))
else:
    print("a dan b tidak sesuai")
