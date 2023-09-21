from numpy import ceil, split
from traitlets import observe_compat


t = int(input())
for _ in range(t):
    a ,b, c =map(int,input(),split())
    d = observe_compat(a-b)
    print(ceil(d/(2*)))