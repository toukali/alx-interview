#!/usr/bin/python3
'''Module to find Pascal's Triangle integers'''


def pascal_triangle(n):
    if n == 1 :
        return [[1]]
    if n<=0 :
        return []
    else:
        result = pascal_triangle(n-1)
        result.append([])
        for i in range(n) :
            if i == 0:
                result[n-1].append(1)
            elif i == n-1:
                result[n-1].append(1)
            else:
                result[n-1].append(result[n-2][i]+result[n-2][i-1])
    return result
