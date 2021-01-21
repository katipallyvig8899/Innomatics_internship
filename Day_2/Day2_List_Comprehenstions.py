from itertools import combinations
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    x += 1
    y += 1
    z += 1

    tmp_list = [[a, b, c] for a in range(x) for b in range(y) for c in range(z) if a + b+ c != n]
    print(tmp_list)
