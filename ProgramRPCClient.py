import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    print("3 is even: %s" % str(proxy.is_even(3)))
    print("100 is even: %s" % str(proxy.is_even(100)))
    
    print('>>>>>>>>>>>>>> Cek Harga <<<<<<<<<<<<<<')
    print("Harga Sabun : %s" % str(proxy.cek_harga_barang('Sabun')))
    print("Harga Deterjen : %s" % str(proxy.cek_harga_barang('Deterjen')))
    print("Harga Sampo : %s" % str(proxy.cek_harga_barang('Sampo')))

    print('>>>>>>>>>>>>>> Transaksi Penjualan <<<<<<<<<<<<<<')
    print("Member Belanja dibawah 100 Ribu: %s" % str(proxy.transaksi(50000,'Y')))
    print("Member Belanja diatas 100 Ribu Disc 20 persen : %s" % str(proxy.transaksi(150000,'Y')))
    print("Bukan Member Belanja : %s" % str(proxy.transaksi(150000,'T')))
