from Values.Constants import Const
from Values.Lbl import Label
from Table import table
from Slicer import slice

res = []
def inputer():
    r = []
    print('Введите внутренний и внешний диаметры слоев начиная с внутреннего')
    for i in range(Const.kc + 1):
        r.append(float(input(f' D{i + 1} = ')))

    be1 = float(input(Label.inpSigmae1)) * Const.k
    pkn = float(input(Label.inpPkn)) * Const.k
    l = float(input(Label.inpL))
    return r, be1, pkn, l


###############################################    Находим оптимальное соотношение слоев
def ratioRad(r):
    be12 = be1 / be2

    a31 = r[1] / r[0]

    a21 = ((2 * (be12 - 1) * (a31 ** 2) / 6 * a31 ** 2 + 1 - be12) + (
            (((2 * (be12 - 1) * a31 ** 2) / (6 * a31 ** 2 + 1 - be12)) ** 2) + (2 * a31 ** 4 * (2 * be12 + 1)) / (
            6 * a31 ** 2 + 1 - be12)) ** 0.5) ** 0.5

    r.append(a21 * r[0])

    return r


r, be1, pkn, l = inputer()

be2 = Const.strengthCategory * be1

r = ratioRad(r)
for i in range(len(r)):
    res.append(r[i])
# res.append(r)
# printer(Label.nameD2, r[2])

# Для простоты написания кода и упрощения формул
a = pow(r[0], 2)
b = pow(r[2], 2)
c = pow(r[1], 2)

slice(l)

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

'''
цикл с нахождением радиусов, зависящим от сечения скрепления, 
переопределить записать каждой переменной в отдельные массивы для удобства последующего вывода, 
захерачить все в tabules, для корректного вывода
'''
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
    Const.arr_q2min.append(q2min / Const.k)
    # printer(Label.nameQ2Min, q2min / Const.k)

    q2max = q2 + Const.dopyskNatyagaMax
    Const.arr_q2max.append(q2max / Const.k)
    # printer(Label.nameQ2Max, q2max / Const.k)

    y2min = q2min / (2 * r2)
    Const.arr_y2min.append(y2min / Const.k)
    # printer(Label.nameY2min, y2min / Const.k)

    y2max = q2max / (2 * r2)
    Const.arr_y2max.append(y2max / Const.k)
    # printer(Label.nameY2max, y2max / Const.k)

    py2 = 1.5 * be2 * ((c - b) / ((2 * c) + b))
    Const.arr_py2.append(py2 / Const.k)
    # printer(Label.namePy2, py2 / Const.k)

    if py2 <= 1.5 * be1 * (a / b):
        p1 = elsticTangDeform(y2min)

    else:
        p1 = elsticRadDeform(y2min)

    Const.arr_p1.append(p1 / Const.k)

    pi2 = Const.E * y2max * ((c - b) * (b - a)) / (2 * b * (c - a))
    Const.arr_pi2.append(pi2 / Const.k)
    # printer(Label.namePi2, pi2 / Const.k)

    pii2 = py2 - pi2
    Const.arr_pii2.append(pii2 / Const.k)
    # printer(Label.namePii2, pii2 / Const.k)

    p21 = pii2 * (b / a) * ((c - a) / (c - b))
    Const.arr_p21.append(p21 / Const.k)
    # printer(Label.nameP21, p21 / Const.k)

    n1 = p1 / pkn
    Const.arr_n1.append(n1)

    n2 = p21 / pkn
    Const.arr_n2.append(n2)

    return res


calk(r[2], be1, pkn)

table(res)
