# for
print("======for=======")
for index in range(1,1 + 1):
    print(f"Index of {index} : Maaf tidak akan mengulang kembali")

list_data = ['nasi', 'Ayam Bakar', 'Daging', 'Ikan', 'Bolu', 'Ikan']
for value in list_data:
    print(f"value of : {value}")
# while
print("=====While===========")
nilai = 11
while nilai <= 10:
    print(f"index of {nilai}")
    nilai += 1

#  break and continue
print("=====break===========")
nilai = 1
while nilai <= 100:
    if nilai % 2 == 0:
        nilai += 1
        continue # skip 1 putaran 
    print(f"Index of {nilai}")
    nilai+=1
    if nilai >= 12:
        break # memberhentikan loop
