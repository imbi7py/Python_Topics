___ pascal(p
    result = []
    for i in range(p
        __ i __ 0:
            result.append([1])
        ____
            result.append([1] + [result[i - 1][j] + result[i - 1][j + 1] for j in range(le.(result[i - 1]) - 1)] + [1])
    r_ result