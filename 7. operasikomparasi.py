# operasi komparasi

# setiap hasil dari operasi komparasi adalah boolean

# >,<,<=,=>,==,!=,is,is not

a = 4
b = 2

# lebih besar dari >
print("================Lebih besar dari=================")
hasil = a > 3
print (a,">",3,"=", hasil)
hasil = b > 3
print (b,">",3,"=", hasil)
hasil = b > 2
print (b,">",2,"=", hasil)

# kurang dari <
print("================Lebih kecil dari=================")
hasil = a < 3
print (a,"<",3,"=", hasil)
hasil = b < 3
print (b,"<",3,"=", hasil)
hasil = b < 2
print (b,"<",2,"=", hasil)

# lebih dari sama dengan >=
print("================Lebih besar dari sama dengan=================")
hasil = a >= 4
print (a,">=",4,"=", hasil)
hasil = b >= 3
print (b,">=",3,"=", hasil)
hasil = b >= 2
print (b,">=",2,"=", hasil)

# kurang dari sama dengan <=
print("================Lebih kecil dari sama dengan=================")
hasil = a <= 4
print (a,"<=",4,"=", hasil)
hasil = b <= 3
print (b,"<=",3,"=", hasil)
hasil = b <= 2
print (b,"<=",2,"=", hasil)

# sama dengan ==
print("================Sama dengan=================")
hasil = a == 4
print (a,"==",4,"=", hasil)
hasil = b == 3
print (b,"==",3,"=", hasil)
hasil = b == 2
print (b,"==",2,"=", hasil)

# tidak sama dengan !=
print("================ tidak sama denganSama dengan=================")
hasil = a != 4
print (a,"!=",4,"=", hasil)
hasil = b != 3
print (b,"!=",3,"=", hasil)
hasil = b != 2
print (b,"!=",2,"=", hasil)

# "is" sebagai komparasi object identity
print("================ object identity is=================")
x = 5 # ini adalah assignment membuat object
y = 5
print("nilai x = ",x, "id = ",hex(id(x)))
print("nilai y = ",y, "id = ",hex(id(y)))
hasil = x is y
print("x is y =", hasil)

# "is not" 
print("================ object identity is=================")
x = 5 # ini adalah assignment membuat object
y = 5
print("nilai x = ",x, "id = ",hex(id(x)))
print("nilai y = ",y, "id = ",hex(id(y)))
hasil = x is not y
print("x is not y =", hasil)

x = 5 # ini adalah assignment membuat object
y = 6
print("nilai x = ",x, "id = ",hex(id(x)))
print("nilai y = ",y, "id = ",hex(id(y)))
hasil = x is not y
print("x is not y =", hasil)
