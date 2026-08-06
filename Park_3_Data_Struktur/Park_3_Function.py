data_kariawan = [
    {
        "nama" : "ucok",
        "tahun_lahir" : 1998,
        "job" : "Programmer",
    },
    {
        "nama" : "siti",
        "tahun_lahir" : 2002,
        "job" : "Desinger",
    },
    {
        "nama" : "zaki",
        "tahun_lahir" : 2000,
        "job" : "Programmer",
    },
    {
        "nama" : "budi",
        "tahun_lahir" : 1996,
        "job" : "Product Manager",
    },
    {
        "nama" : "Asep Karbu",
        "tahun_lahir" : 1999,
        "job" : "Programmer",
    },
]

# function
# void
def template_print(nama,job,usia:int=3):
    print("==================")
    print(f"Nama\t: {nama}")
    print(f"Job\t: {job}")
    print(f"Usia\t: {usia} tahun")
    
# non void
def usia_kariawan(tahun_lahir):
    hasil = 2026 - tahun_lahir
    return hasil

data_kariawan[0]["usia"] = usia_kariawan(data_kariawan[0]["tahun_lahir"])
data_kariawan[1]["usia"] = usia_kariawan(data_kariawan[1]["tahun_lahir"])
data_kariawan[2]["usia"] = usia_kariawan(data_kariawan[2]["tahun_lahir"])
data_kariawan[3]["usia"] = usia_kariawan(data_kariawan[3]["tahun_lahir"])
data_kariawan[4]["usia"] = usia_kariawan(data_kariawan[4]["tahun_lahir"])


template_print(data_kariawan[0]["nama"],data_kariawan[0]["job"],data_kariawan[0]["usia"])
template_print(data_kariawan[1]["nama"],data_kariawan[1]["job"],data_kariawan[1]["usia"])
template_print(data_kariawan[2]["nama"],data_kariawan[2]["job"],data_kariawan[2]["usia"])
template_print(data_kariawan[3]["nama"],data_kariawan[3]["job"],data_kariawan[3]["usia"])
template_print(data_kariawan[4]["nama"],data_kariawan[4]["job"],data_kariawan[4]["usia"])



