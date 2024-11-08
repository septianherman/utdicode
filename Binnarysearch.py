def pencarianBiner(data, kunci,low,high):
    while (low<=high):
        middle = (low+high)//2
        if (kunci==data[middle]):
            return middle
        elif (kunci<data[middle]):
            high = middle-1
        else:
            low = middle+1
        return -1

data = [12, 23, 38, 42, 59, 67]
print("Masukkan data yang dicari ")
x = int(input())
hasil = pencarianBiner(data, x, 0, len(data)-1)
if (hasil>=0):
    print("Data ditemukan")
else:
    print("Data tidak ditemukan")