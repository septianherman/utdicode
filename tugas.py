belanja = float(input("Masukan total belanja :"))
status_anggota = input("Apakah anda anggota ? (ya/tidak)").lower()

diskon =0

if belanja >=200000:
        if status_anggota == "ya" :
            diskon = belanja * 0.2
        else:
            diskon = belanja * 0.1
     
bayar = belanja - diskon

print("Total Belanja :",belanja)
print("Diskon :",diskon)
print("Bayar :",bayar)

   