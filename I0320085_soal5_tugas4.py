s = "Roti dipanggang oven"

#Panjang string 20
print("Panjang dari s = %d" % len(s))

#Huruf pertama 'a' harusnya di index no 8
print("Kemunculan pertama a =  %d" % s.index("a"))

#Jumlah huruf 'a' harusnya 2
print("a muncul sebanyak %d kali" % s.count("a"))

#Memotong string berdasarkan index
print("Lima karakter pertama adalah '%s'"% s[:5])       # Start to 5
print("Lima karakter berikutnya adalah '%s'"% s[5:10])  # 5 to 10
print("Karakter ketiga belas adalah '%s'" % s[12])      # Just number 12
print("Karakter dengan indeks ganjil '%s'" % s[1::2])   # 0-based indexing
print("Lima karakter terakhir adalah '%s'" % s[-5:])    # 5th-last to end

#Konversikan ke upercase
print("String dalam huruf besar: %s" % s.upper())

#Konversikan ke lowercase
print("String dalam huruf kecil: %s" % s.lower())

#Cek bagaimana string itu dimulai
if s.startswith("Rot"):
    print("String dimulai dengan 'Roti'. Good!")

#Cek bagaimana string itu diakhiri
if s.endswith("ven"):
    print("String diakhiri dengan 'oven'. Good!")

#Pisahkan string menjadi tiga string yang terpisah dan hanya satu kata
print("Pisahkan kata-kata dari string tersebut: %s" % s.split(" "))
