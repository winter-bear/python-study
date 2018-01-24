def triangles():
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a,a + [0])]

if __name__ == '__main__':
    h = int(input('请输入您要显示的最大行数：'))
    tri = triangles()
    for n in range(h):
        print(next(tri))
