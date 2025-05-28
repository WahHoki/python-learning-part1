import datetime as dt

print("Silakan masukkan tanggal, \nbulan dan tahun")
tanggal = int(input("Tanggal \t : "))
bulan = int(input("Bulan \t\t : "))
tahun = int(input("Tahun \t\t : "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal lahir Anda : {tanggal_lahir}")
print(f"Harinya adalah : {tanggal_lahir:%A}")

hari_ini = dt.date.today()
print(f"Hari ini tanggal : {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365 ## left division
umur_bulan_sisa = (umur_hari.days % 365) // 30

print(umur_hari)
print(f"Umur Anda adalah : {umur_tahun} tahun, {umur_bulan_sisa} bulan")
