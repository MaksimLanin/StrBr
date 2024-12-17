from Values.Constants import Const
from Values.Lbl import Label
from Table import table
res = []


def inputer():
    r = []
    print('Введите внутренний и внешний диаметры слоев начиная с внутреннего')
    for i in range(Const.kc + 1):
        r.append(float(input(f' D{i + 1} = ')))

    be1 = float(input(Label.inpSigmae1)) * Const.k
    pkn = float(input(Label.inpPkn)) * Const.k

    return r, be1, pkn


def printer(name, ):
    print(round(name, 3), end = '  ' )


###############################################    Находим оптимальное соотношение слоев
def ratioRad(r):
    be12 = be1 / be2

    a31 = r[1] / r[0]

    a21 = ((2 * (be12 - 1) * (a31 ** 2) / 6 * a31 ** 2 + 1 - be12) + (
            (((2 * (be12 - 1) * a31 ** 2) / (6 * a31 ** 2 + 1 - be12)) ** 2) + (2 * a31 ** 4 * (2 * be12 + 1)) / (
            6 * a31 ** 2 + 1 - be12)) ** 0.5) ** 0.5

    r.append(a21 * r[0])

    return r


r, be1, pkn = inputer()

be2 = Const.strengthCategory * be1

r = ratioRad(r)
res.append(r[2])
# printer(Label.nameD2, r[2])

# Для простоты написания кода и упрощения формул
a = pow(r[0], 2)
b = pow(r[2], 2)
c = pow(r[1], 2)


# расчёт предела упругого сопротивления трубы и тангенциального натяжения ведут по формуле для максимальных тангенциальных деформаций
def tangtangDeform():
    # Расчёт условного предела упругого сопротивления трубы
    py1 = 1.5 * be1 * ((b - a) / ((2 * b) + a)) + (1.5 * be2) * ((3 * b) / (
            (2 * b) + a)) * ((c - b) / ((2 * c) + b))
    # тангециальное сжатие на внутренней поверхности канала ствола от скрепления.
    tp1 = (2 / 3) * py1 * (((2 * c) + a) / (c - a)) - be1
    return py1, tp1


# расчёт предела упругого сопротивления трубы и тангенциального натяжения ведут по формуле для максимальных радиальных деформаций
def tangradDeform():
    # Расчёт условного предела упругого сопротивления трубы
    py1 = 1.5 * be1 * ((b - a) / ((2 * b) - a)) + 1.5 * be2 * (b / (
            (2 * b) - a)) * ((c - b) / ((2 * c) + b))
    # тангециальное сжатие на внутренней поверхности канала ствола от скрепления.
    tp1 = 2 * py1 * (((2 * c) - a) / (c - a)) - 3 * be1
    return py1, tp1


# Расчёт предела упругого сопротивления первого слоя по максимальным тангенциальным деформациям
def elsticTangDeform(y2min):
    p1 = 1.5 * (be1 + Const.E * y2min * ((c - b) / (c - a))) * ((c - a) / ((2 * c) + a))
    # printer(Label.nameP1Tang, p1 / Const.k)
    return p1


# Расчет предела упругого сопротивления первого слоя по максимальным радиальным деформациям

def elsticRadDeform(y2min):
    p1 = 1.5 * (be1 + (1 / 3) * Const.E * y2min * ((c - b) / (c - a))) * ((c - a) / ((2 * c) - a))
    # printer(Label.nameP1Rad, p1 / Const.k)
    return p1


###################################################   Определение оптимального натяга между слоями
def calk(r2, be1, pkn, ):
    # Предел упругого сопротивления кожуха
    py2 = 1.5 * be2 * ((c - b) / ((2 * c) + b))

    if py2 <= (0.75 * be1 * (a / b)):
        py1, tp1 = tangtangDeform()

    else:
        py1, tp1 = tangradDeform()

    # Абсолютные расчётные натяжения
    q2 = 2 * r2 * ((tp1 * (c - a)) / (Const.E * (c - b)))

    ###################################################   Проверка прочности скреплённого ствола

    q2min = q2 + Const.dopyskNatyagaMin
    res.append(q2min / Const.k)
    # printer(Label.nameQ2Min, q2min / Const.k)

    q2max = q2 + Const.dopyskNatyagaMax
    res.append(q2max / Const.k)
    # printer(Label.nameQ2Max, q2max / Const.k)

    y2min = q2min / (2 * r2)
    res.append(y2min / Const.k)
    # printer(Label.nameY2min, y2min / Const.k)

    y2max = q2max / (2 * r2)
    res.append(y2max / Const.k)
    # printer(Label.nameY2max, y2max / Const.k)

    py2 = 1.5 * be2 * ((c - b) / ((2 * c) + b))
    res.append(py2 / Const.k)
    # printer(Label.namePy2, py2 / Const.k)

    if py2 <= 1.5 * be1 * (a / b):
        p1 = elsticTangDeform(y2min)

    else:
        p1 = elsticRadDeform(y2min)

    res.append(p1 / Const.k)

    pi2 = Const.E * y2max * ((c - b) * (b - a)) / (2 * b * (c - a))
    res.append(pi2 / Const.k)
    # printer(Label.namePi2, pi2 / Const.k)

    pii2 = py2 - pi2
    res.append(pii2 / Const.k)
    # printer(Label.namePii2, pii2 / Const.k)

    p21 = pii2 * (b / a) * ((c - a) / (c - b))
    res.append(p21 / Const.k)
    # printer(Label.nameP21, p21 / Const.k)

    n1 = p1 / pkn
    res.append(n1)

    n2 = p21 / pkn
    res.append(n2)


calk(r[2], be1, pkn)

table(res)
