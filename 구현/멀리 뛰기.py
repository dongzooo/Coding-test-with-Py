def solution(n):
    if n < 3:
        return 1
    a, b = 1, 2
    for i in range(2,n):
        a, b = b, a+b
    print(b)
    print(b%1234567)
    return b%1234567
