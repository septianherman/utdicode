def SelectionSort(val):
    for isi in range(0,len(val),1):
        min=isi
        for lokasi in range(isi+1,len(val),1):
            if val[lokasi]<val[min]:
                min = lokasi
            temp = val[isi]
            val[isi] = val[min]
            val[min] = temp
DaftarAngka = [23,7,32,99,4,15,11,20]
SelectionSort(DaftarAngka)
print(DaftarAngka)