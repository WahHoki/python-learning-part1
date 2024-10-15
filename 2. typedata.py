# a = 10, a adalah variabel dengan nilai 10

# type data: angka satuan (integer)
data_integer = 1
print("data = ", data_integer)
print(" bertype : ", type(data_integer))

# type data: angka dengan koma(float)
data_float = 1.4
print("data = ", data_float)
print(" bertype : ", type(data_float))

# type data: kumpulan karakter (string)
data_string = "hallo dek"
print("data = ",  data_string)
print("bertype = ", type(data_string))

# type data: biner true/false (boolean)
data_boolean = True
print ("data = ", data_boolean)
print ("bertype = ", type(data_boolean))

# type data: didefinisikan dengan tanda kurung (tuple)
data_tupel = 1,3
print ("data = ", data_tupel)
print ("bertype = ",type(data_tupel))

## type data khusus

# bilangan kompleks
data_complex = complex(1,2)
print("data = ", data_complex)
print("bertype = ", type(data_complex))

# tipe data dari bahasa c (c_double, c_char, c_long)
from ctypes import c_double

data_c_double = c_double(10.5)
print ("data = ", data_c_double)
print ("bertype = ", type(data_c_double))
