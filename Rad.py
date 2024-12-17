
def calkRad(d, kc=1, kt=11):
    r = []
    for i in range(kc + 1):
        if len(d) == i + 1:
            break
        h = 0.5 * (d[i + 1] - d[i]) / (kt - 1)
        for l in range(kt + 1):
            r.append(0.5 * d[i] + h * (l - 1))




