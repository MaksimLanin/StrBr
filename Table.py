from tabulate import tabulate
from Values.Constants import Const


def table(res):
    data = [
        [Const.arr_l[0], res[0], res[1], res[2], Const.arr_q2min[0], Const.arr_q2max[0],
         Const.arr_y2min[0], Const.arr_y2max[0], Const.arr_py2[0],
         Const.arr_p1[0], Const.arr_pi2[0], Const.arr_pii2[0],
         Const.arr_p21[0], Const.arr_n1[0], Const.arr_n2[0]],

        [Const.arr_l[1], res[0], res[1], res[2], Const.arr_q2min[0], Const.arr_q2max[0],
         Const.arr_y2min[0], Const.arr_y2max[0], Const.arr_py2[0],
         Const.arr_p1[0], Const.arr_pi2[0], Const.arr_pii2[0],
         Const.arr_p21[0], Const.arr_n1[0], Const.arr_n2[0]],

        [Const.arr_l[2], res[0], res[1], res[2], Const.arr_q2min[0], Const.arr_q2max[0],
         Const.arr_y2min[0], Const.arr_y2max[0], Const.arr_py2[0],
         Const.arr_p1[0], Const.arr_pi2[0], Const.arr_pii2[0],
         Const.arr_p21[0], Const.arr_n1[0], Const.arr_n2[0]],

        [Const.arr_l[3], res[0], res[1], res[2], Const.arr_q2min[0], Const.arr_q2max[0],
         Const.arr_y2min[0], Const.arr_y2max[0], Const.arr_py2[0],
         Const.arr_p1[0], Const.arr_pi2[0], Const.arr_pii2[0],
         Const.arr_p21[0], Const.arr_n1[0], Const.arr_n2[0]],

        [Const.arr_l[4], res[0], res[1], res[2], Const.arr_q2min[0], Const.arr_q2max[0],
         Const.arr_y2min[0], Const.arr_y2max[0], Const.arr_py2[0],
         Const.arr_p1[0], Const.arr_pi2[0], Const.arr_pii2[0],
         Const.arr_p21[0], Const.arr_n1[0], Const.arr_n2[0]],

        [Const.arr_l[5], res[0], res[1], res[2], Const.arr_q2min[0], Const.arr_q2max[0],
         Const.arr_y2min[0], Const.arr_y2max[0], Const.arr_py2[0],
         Const.arr_p1[0], Const.arr_pi2[0], Const.arr_pii2[0],
         Const.arr_p21[0], Const.arr_n1[0], Const.arr_n2[0]],

        [Const.arr_l[6], res[0], res[1], res[2], Const.arr_q2min[0], Const.arr_q2max[0],
         Const.arr_y2min[0], Const.arr_y2max[0], Const.arr_py2[0],
         Const.arr_p1[0], Const.arr_pi2[0], Const.arr_pii2[0],
         Const.arr_p21[0], Const.arr_n1[0], Const.arr_n2[0]],

        [Const.arr_l[7], res[0], res[1], res[2], Const.arr_q2min[0], Const.arr_q2max[0],
         Const.arr_y2min[0], Const.arr_y2max[0], Const.arr_py2[0],
         Const.arr_p1[0], Const.arr_pi2[0], Const.arr_pii2[0],
         Const.arr_p21[0], Const.arr_n1[0], Const.arr_n2[0]],

        [Const.arr_l[8], res[0], res[1], res[2], Const.arr_q2min[0], Const.arr_q2max[0],
         Const.arr_y2min[0], Const.arr_y2max[0], Const.arr_py2[0],
         Const.arr_p1[0], Const.arr_pi2[0], Const.arr_pii2[0],
         Const.arr_p21[0], Const.arr_n1[0], Const.arr_n2[0]],

        [Const.arr_l[9], res[0], res[1], res[2], Const.arr_q2min[0], Const.arr_q2max[0],
         Const.arr_y2min[0], Const.arr_y2max[0], Const.arr_py2[0],
         Const.arr_p1[0], Const.arr_pi2[0], Const.arr_pii2[0],
         Const.arr_p21[0], Const.arr_n1[0], Const.arr_n2[0]],

        [Const.arr_l[10], res[0], res[1], res[2], Const.arr_q2min[0], Const.arr_q2max[0],
         Const.arr_y2min[0], Const.arr_y2max[0], Const.arr_py2[0],
         Const.arr_p1[0], Const.arr_pi2[0], Const.arr_pii2[0],
         Const.arr_p21[0], Const.arr_n1[0], Const.arr_n2[0]],

        [Const.arr_l[11], res[0], res[1], res[2], Const.arr_q2min[0], Const.arr_q2max[0],
         Const.arr_y2min[0], Const.arr_y2max[0], Const.arr_py2[0],
         Const.arr_p1[0], Const.arr_pi2[0], Const.arr_pii2[0],
         Const.arr_p21[0], Const.arr_n1[0], Const.arr_n2[0]]

    ]

    tab = tabulate(
        data,
        tablefmt="fancy_grid",
        headers=['L', 'D1', 'D3', 'D2', 'q2min', 'q2max', 'y2min', 'y2max', 'Py2', 'P1', 'Pi2', 'Pii2', 'P21', 'n1',
                 'n2'],
        numalign="center",
        stralign="center",
    )

    print(tab)


'''
data = [
    [l[0], d1[0], d3[0], и тд],
    [l[1], d1[1], d3[1], и тд],
    и тд 
    ]
    
'''
