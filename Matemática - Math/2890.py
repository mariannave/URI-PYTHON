'''
Entradas:
1
8
2250
123
0
Saída:
1
400
878008
87622
'''

if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break
        n2 = n * n
        n4 = n2 * n2

        print((11 * n2 + n4) // 12 % 1000007)
