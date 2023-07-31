def luas(j):
  luas_lingkaran = 3.14 * j * j
  return luas_lingkaran

def keliling(j):
  keliling_lingkaran = 2 * 3.14 * j
  return keliling_lingkaran

#nama : fara azzura dasgupta , kelas : x rpl 2
print("program menghitung luas dan keliling lingkaran :")
print("================================================") 
j = int(input("jari_jari : \t"))
print("hasil luas : \t" , luas(j))
print("hasil keliling : \t" , keliling(j))