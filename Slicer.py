from Values.Constants import Const
def slice(l):

    sl = int(l / 10)

    for i in range(0, int(l + 1), sl):
        Const.arr_l.append(round(i, 2))
    if Const.arr_l[-1] != l:
        Const.arr_l.append(l)
    print(Const.arr_l)

