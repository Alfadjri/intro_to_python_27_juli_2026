import datetime

tanggal = datetime.datetime.now()
nama_manager = "Alfadjri"
pt = "PT Semua Mahir Teknologi"

# posisional argument
print("===========")
print("\t\t{0}\nYth.{1}\n{2}".format(tanggal,pt,nama_manager))
print("===========")
# keyword argument
print("===========")
print("\t\t{tanggal}\nYth.{nama_manager}\n{pt}".format(tanggal=tanggal,pt=pt,nama_manager=nama_manager))
# singkatan
print("===========")
print(f"\t\t{tanggal}\nYth.{nama_manager}\n{pt}")