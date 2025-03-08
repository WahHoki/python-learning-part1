# pengenalan string
data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string
'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote '...'
'''

data = "Menggunakan quote single"
print(data)

data = "Menggunakan quote double"
print(data)

print('"hallo, apa kabar?"')
print("'hallo, apa kabar?'")
print("ini adalah hari rabu")

# 2. menggunakan tanda \

# membuat tanda ' menjadi string
print('mari berd\'oa')
print('g\'day, isn\'t it?')

# blacklash
print("C:\\user\\ucup")

# tab
print("ucup\t\t\totong, semakin jauhan")

# backspace
print("ucup \botong, jadi deketan")

# newline 
print("baris pertama. \nbaris kedua.") # LF -> line feed -> unix,  macos, linux
print("baris pertama. \rbaris kedua.") # CR -> carriage return -> commodere, acorn, lisp
print("baris pertama. \r\nbaris kedua.") #CRLF -> Line feed carriage return -> dipakai oleh windows

# 3. string literal atau raw

# hati-hati
print('C:\new folder') # akan salah pastinya

# menggunakan raw string
print(r'C:\new folder')

# multiline literal raw string
print("""
Nama : Ucup
Kelas : 3 SD
""")

# multiline literal string dan RAW
print(r"""
Nama : Ucup 
Kelas : 3 SD
Website : www.ucup.com/newID
""")
