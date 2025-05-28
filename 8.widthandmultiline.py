# width dan multiline

# data 
data_nama = "ucup surotong"
data_umur = 17
data_tinggi = 150.1
data_nomor_sepatu = 43

# string
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu}"
print(5*"="+"Data string"+5*"=")
print(data_string)

# string multiline (dengan menggunakan enter, newline, \n)
data_string = f"\nnama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nsepatu = {data_nomor_sepatu}"
print("\n"+5*"="+"Data string"+5*"=")
print(data_string)

# string multiline (kutip triplets)
data_string = f"""
nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""

print("\n"+5*"="+"Data string"+5*"=")
print(data_string)

# mengatur lebar
data_nama = "ucup"
data_string = f"""
nama = {data_nama:<5}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""

print("\n"+5*"="+"Data string"+5*"=")
print(data_string)
