# Create
data_kelas = {
    "nama_kelas" : 12,
    "Jurusan" : ["IPA","IPS","Bahasa"],
    "nama_ketua" : "Ucok"
}

# Create
print(f"Read All : {data_kelas}")
print(f"Nama ketua kelas : {data_kelas["nama_ketua"]}")
print(f"Jurusan IPS : {data_kelas["Jurusan"][1]}")
# Append
data_kelas["Jumlah_siswa"] = 40
print(f"Read All : {data_kelas}")
# Update
data_kelas["nama_kelas"] = 10
print(f"Read Al : {data_kelas}")
# Delete
del data_kelas["Jumlah_siswa"]
print(f"Read All : {data_kelas}")
