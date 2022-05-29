def main():
    ex1 = 1
    ex2 = 2
    ex3 = 3

    res_1 = bellNumber(ex1)
    res_2 = bellNumber(ex2)
    res_3 = bellNumber(ex3)

    print(res_1)
    print(res_2)
    print(res_3)


def bellNumber(n):
    bell = [[0 for i in range(n)] for j in range(n)]
    bell[0][0] = 1
    for i in range(1, n):
        bell[i][0] = bell[i-1][i-1]
        for j in range(1, i+1):
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]

    return bell[n-1][-1]


if __name__ == "__main__":
    main()