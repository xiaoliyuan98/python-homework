def Joseph(n,k):
    a = [x for x in range(1, n+1)]
    num = k
    for i in range(n):
        print(a[num%len(a)-1])
        del a[num%len(a)-1]
        if len(a)==0:
            print('ok')
        else:
            num = (num + k-1) % len(a)

Joseph(10, 7)