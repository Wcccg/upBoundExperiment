import math
import datetime
from getData import *
from readFile import *
from compute import *

if __name__ == '__main__':

    nn = 60
    sumUU = 0.9
    mul = 10000
    TTmax, TTmin = getTmax(nn, sumUU, mul)
    percent = 0
    i = 100
    while i:
        U = getU(nn, sumUU)
        T = getT(nn, mul, TTmin)
        C, T, sumU = getC(nn, U, T, TTmax, TTmin)
        D = getD(nn, C, T)
        writefile('aurg.txt', C, D, T, nn, sumU, TTmax)
        n, sumU, Tmax, Tmin = readbase('aurg.txt')
        if int(Tmax / Tmin) > 1.1 * mul or int(Tmax / Tmin) < 0.9 * mul:
            continue
        else:
            i -= 1
        print(100 - i, 'th', ', n = ', n, ', sumU = ', sumU, ', Tmax / Tmin= ', int(Tmax / Tmin))
        C, D, T = readsample('aurg.txt')
        task = readTask('aurg.txt')
        L = getL(C, D, T, sumU, n)
        dmin = getdmin(D, T, n)

        t1 = datetime.datetime.now() - datetime.datetime.now()
        t2 = datetime.datetime.now() - datetime.datetime.now()
        for j in range(0, 100):
            startTime2 = datetime.datetime.now()
            flag2, count2 = useQPA(C, D, T, n, dmin, L)
            endTime2 = datetime.datetime.now()
            t2 += endTime2 - startTime2
            startTime1 = datetime.datetime.now()
            flag1, count1 = useGreaterDistance(task, n, dmin, L)
            endTime1 = datetime.datetime.now()
            t1 += endTime1 - startTime1
        # print('QPAcount = ', count2, 'time =',  t2)
        # print('Discount = ', count1, 'time =',  t1)
        if t1 < t2:
            percent += 1
    print('percent = ', percent, '%\n')
    # print('QPAcount = ', count2, 'time =',  t2)
    # print('Discount = ', count1, 'time =',  t1)
    # if flag1 == 0:
    #     print('schedulable')
    # else:
    #     print('unschedulable')

