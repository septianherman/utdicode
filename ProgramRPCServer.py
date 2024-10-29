from xmlrpc.server import SimpleXMLRPCServer

def is_even(n):
    return n % 2 == 0

def cek_harga_barang(nama_barang):
    if nama_barang=='Sabun':
        return 10000
    elif nama_barang=='Deterjen':
        return 5000
    elif nama_barang=='Sampo':
        return 20000
    else:
        return 0
    

def transaksi(total,member):
    discount=0.2
    if member=='Y':
        if total>=100000:
            return total - (total*discount)
        else:
            return total
    else:
        return total   

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(is_even, "is_even")
server.register_function(cek_harga_barang, "cek_harga_barang")
server.register_function(transaksi, "transaksi")
server.serve_forever()