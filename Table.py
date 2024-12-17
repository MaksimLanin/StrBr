from tabulate import tabulate


def table(res):
    data = [
        [res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7], res[8], res[9], res[10], res[11]]
    ]

    tab = tabulate(
        data,
        tablefmt="fancy_grid",
        headers=['D2', 'q2min', 'q2max', 'y2min', 'y2max', 'Py2', 'P1', 'Pi2', 'Pii2', 'P21', 'n1', 'n2'],
        numalign="center",
        stralign="center",
    )

    print(tab)
