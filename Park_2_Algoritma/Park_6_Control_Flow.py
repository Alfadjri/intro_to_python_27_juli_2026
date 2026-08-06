nilai = 80

print("==== IF Statemen ====")
if nilai > 80 :
    print("Selamat kamu lulus Test ini")

print("==== IF Else Statemen ==")
if nilai > 80 :
    #code
    print("Selamat kamu lulus Test ini")
else :
    #code
    print("Mohon maaf kamu tidak lulus")

print("==== IF Elif Else Statemen ====")
if nilai >= 91:
    print("Nilai : A")
elif nilai >= 71 and nilai < 90:
    print("Nilai : B")
elif nilai >= 60 and nilai < 70 :
    print("Nilai : C")
else :
    print("Mohon maaf kamu tidak lulus")

print("if Nested (if Bersarang)")
nilai = 85
if nilai > 80:
    # code
    # code
    if nilai > 90:
        # code
        print("Nilai bagus")
        # code
    else :
        print("nilai kurang")

print("if Tenery")
kk = "Sudah ada" if nilai > 70 else "Tidak ada"
print(kk)

print("====match and case===")
print("===== Menu ====")
print("1. Start")
print("2. Exit")
select = int(input("Select =>>"))
match select:
    case 1:
        print("start")
    case 2:
        print("Exit")
    case _:
        print("Invalid input type")
