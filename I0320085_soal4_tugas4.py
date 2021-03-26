import time
run = time.time()

#Input pertanyaan
x = int(input('Berapa usia Anda?'))
y = input('Apakah Anda sudah lulus ujian kualifikasi (Y/T)?')

#Output
if x >= 21 and y == "Y":
    print('Anda dapat mendaftar di kursus.')
else:
    print('Anda tidak dapat mendaftar di kursus.')

print("Waktu runtime :", time.time() - run, "detik")