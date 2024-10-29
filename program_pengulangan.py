import os
lagi='Y'
while lagi=='Y' or lagi=='y':
    os.system('cls')
    n = int(input('Masukan jumlah loop:'))
    j=0
    for i in range(n):
        x=int(input('masukan nilai x ke : ',format(i)))
        j=j+x
    print('Jumlah=',j)
    print()    
    