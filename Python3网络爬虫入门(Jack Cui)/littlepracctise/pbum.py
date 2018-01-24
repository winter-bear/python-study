def pnum():
    p = int(input("请输入一个正整数："))
    num_pnum =0
    lpnum = []
    for num in range(2,p):
        result = []
        flag = num       #打印标志位
        for factor in range(1,num):
            if num % factor == 0:
                flag -= factor
                result.append(factor)
        if flag == 0:
            print(num,end='=')
            result_length = len(result)
            for i in range(result_length):
                if i != result_length - 1:
                    print(result[i],end='+')
                else:
                    print(result[i])
            num_pnum =num_pnum+1
            print("发现一个完备数")
            lpnum.append(num)
    print('总计有%d个完备数，分别是：'%num_pnum)
    for i in lpnum:
        print(i,end='\t')
if __name__ == '__main__':
    pnum()
