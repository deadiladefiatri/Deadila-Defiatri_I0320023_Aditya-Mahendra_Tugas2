
print ("-----Menentukan Luas Persegi Panjang-----")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("")
panjang = float(input("Masukkan panjang : "))
lebar = float(input("Masukkan Lebar : "))
luas = panjang*lebar
print ("luas persegi panjang adalah", luas, "satuan")
print ("")

print ("-----Menghitung Luas Lingkaran------")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("")
jari_jari = float(input("Masukkan jari _jari : " ))
phi = 3.14
luaslingkaran = jari_jari*jari_jari*phi
print ("luas lingkaran", luaslingkaran , "satuan" )
print("")

print ("-----Menghitung Luas Permukaan Kubus-----")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("")
sisi = float(input("Masukkan panjang sisi = "))
LuasPermukaanKubus = 6*sisi*sisi
print ("Luas Permukaan Kubus adalah", LuasPermukaanKubus, "satuan")

print("")
print ("-----KONVERSI SUHU CELCIUS KE FAHREINHEIT-----")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("")
C = float(input ("Masukkan suhu dalam ºC = "))
F = ((9/5)*C) + 32
print ("Suhu dalam ºF =", F )
print("")
print ("-----KONVERSI SUHU REAMUR KE FAHREINHEIT-----")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("")
R = float(input ("Masukkan suhu dalam ºR = "))
K = ((5/4)*R) + 273
print ("Suhu dalam ºK = ", K )
