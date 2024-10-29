import os
# Loop menurun dari 10 ke -10
for i in range(10, -11, -1):
    print(i,end=" ")

# Inisialisasi total
total = 0

# Daftar pecahan yang ingin dihitung
pecahan = [1/2, 1/3, 1/4, 1/5]

# Loop untuk menghitung total
for angka in pecahan:
    total += angka

# Cetak hasil total
print("Hasil dari 1/2 + 1/3 + 1/4 + 1/5 adalah:", total)

i = int(input('Masukan bilangan'))
for x in i:
    for y in range(5):
        t = x*y
        print(x,y,t)


