def BubbleSort(val):
    for passnum in range(len(val)-1,0,-1): #range dari akhir daftar sampai awal, step -1 (turun)
        for i in range(len(val)-passnum,0,-1):
            if val[i]<val[i-1]:
                temp = val[i]
                val[i] = val[i-1]
                val[i-1] = temp

DaftarAngka = [23,7,32,99,4,15,11,20]
BubbleSort(DaftarAngka)
print(DaftarAngka)