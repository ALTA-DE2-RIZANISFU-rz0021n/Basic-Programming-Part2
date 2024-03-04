'''
Input Harga: 370000
Input Diskon: 15
Output: harga yang harus dibayar adalah Rp. 314.500
'''

harga_awal = int(input('masukkan harga produk: '))
diskon = int(input('masukkan harga diskon: '))

harga_akhir = int((100-diskon)/100*harga_awal)
print('Harga setelah diskon: ', harga_akhir)