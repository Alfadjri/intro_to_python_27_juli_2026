#inisialisasi
makanan = ["nasi","Ayam Bakar","Daging","Bolu"]
#CRUD
# C craete (Kak data tidak simpan)

# R Read (Kak Lodingnya lama)
print(f"List All : {makanan}")
print(f"Memanggil Daging : {makanan[2]}")
# U Update (Kak ini kok gak bisa di ubah)
makanan[3] = "Ikan"
print(f"List All : {makanan}")
# A Append
makanan.append("Bolu")
makanan.append("Ikan")
print(f"List All : {makanan}")
# D Delete (Kak udah di hapus bisa di balikin lagi gak ? )
del makanan[1]
print(f"List All : {makanan}")
