while 1 :
    a = list(map(int,input().split()))
    max_num = max(a)
    a.remove(max_num)
    if sum(a) == 0:
        break
    else :
        if a[0]**2 + a[1]**2 == max_num**2 :
            print("right")
        else :
            print("wrong")
