from math import ceil

t = int(input())

for _ in range(t):
    a, b, c = map(int,input().split())        

    d = abs(a-b)                            
    print(ceil(d / (2*c)))