#Pengulangan String
daftarbuah = ["Apel","Mangga","Semangka","Belimbing","Tomat"]
print(daftarbuah,'\n')
print('tampilkan menggunakan loop')
for x in daftarbuah:
    if x == 'Mangga':
        continue
    print(x)
    
print('>>>>>>Selesai String<<<<<<<')

#Pengulangan Integer
print(range(5,10),'\n')
for x in range(5,10):
    print(x,end=" ")

print('>>>>>>Selesai Integer<<<<<<<')

#Pernyataan For Else
for x in range(5):
    print('Langkah :',x+1)
else :
    print('Bagian Blok Else')

print('>>>>>>Selesai For Else<<<<<<<')

#Loop di Dalam Loop
for x in range(4):
    for y in range(3):
        print(x,y)

print('>>>>>>Selesai Multi Loop<<<<<<<')

#Loop While Break
i=1
while i < 6:
    print(i)
    if i==3:
        break
    i+=1

print('>>>>>>Selesai While Loop Break<<<<<<<')

#Loop While Continue
i=1
while i < 6:
    if i==3:
       continue
    print(i)
    i+=1
print('>>>>>>Selesai While Loop Continue<<<<<<<')