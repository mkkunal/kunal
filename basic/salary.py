bs=int(input("total salary is -:>"))
if bs<=10000:
    Hra=0.3*bs
    da=bs*0.8
    Total=bs+Hra+da
    print("total salary is",Total)
elif bs<=20000:
    Hra=0.25*bs
    da=bs*0.9
    Total=bs+Hra+da
    print("total salary is",Total)
else:
    bs > 20000
    Hra = 0.3 * bs
    da = bs * 0.95
    Total = bs + Hra + da
    print("total salary is", Total)