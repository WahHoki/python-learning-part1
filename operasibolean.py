# operasi logika atau bolean

# not, or, and ,xor

# not
print("=====NOT=====")
a = True
c = not a
print("data a = ", a)
print("-----------NOT")
print("data c = ", c)

# jika salah satu true, maka hasilnya adalh true (or)
print("=====OR=====")
a = False
b = False
c = a or b
print(a, " OR ", b, "=", c)
a = True
b = True
c = a or b
print(a, " OR ", b, "=", c)
a = False
b = True
c = a or b
print(a, " OR ", b, "=", c)
a = True
b = False
c = a or b
print(a, " OR ", b, "=", c)

# jika dua buah nilai true, maka hasil menjadi true (and)
print("=====AND=====")
a = False
b = False
c = a and b
print(a, " AND ", b, "=", c)
a = True
b = True
c = a and b
print(a, " AND ", b, "=", c)
a = False
b = True
c = a and b
print(a, " AND ", b, "=", c)
a = True
b = False
c = a and b
print(a, " AND ", b, "=", c)

# akan true jika salah satu true dan sisanya false (XOR)
print("=====XOR=====")
a = False
b = False
c = a ^ b
print(a, " XOR ", b, "=", c)
a = True
b = True
c = a ^ b
print(a, " XOR ", b, "=", c)
a = False
b = True
c = a ^ b
print(a, " XOR ", b, "=", c)
a = True
b = False
c = a ^ b
print(a, " XOR ", b, "=", c)