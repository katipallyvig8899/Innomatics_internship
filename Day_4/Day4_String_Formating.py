def print_formatted(number):
    s = len("{0:b}".format(number))

    for i in range(number):
        e = "{0:%id} {0:%io} {0:%iX} {0:%ib}" % (s, s, s, s)
        print(e.format(i+1))
