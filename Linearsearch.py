data = [12, 20, 14, 9, 34]
print("Masukan Data yang dicari = ")
x = int(input())
for i in range(len(data)) :
    if (data[i] == x) :
        print("Data tersebut ada pada posisi ke-"
,i)
    break
else :
    print("Data tidak ketemu !")