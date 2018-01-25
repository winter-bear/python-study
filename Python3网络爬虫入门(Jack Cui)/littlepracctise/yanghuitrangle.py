def triangles():
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a,a + [0])]
        ##print(a)

if __name__ == '__main__':
    h = int(input('请输入您要显示的最大行数：'))
    tri = triangles()
    for n in range(h):
        print(next(tri))
'''
def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]

n=0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
'''