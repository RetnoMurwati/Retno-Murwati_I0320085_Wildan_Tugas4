#Berat maksimum bagasi
x = 50              # x adalah berat bagasi dalam satuan lbs
y = x * 0.454       # y adalah berat bagasi dalam satuan kg
print('Berat maksimum bagasi adalah', y, 'kg')

#Input berat bagasi dalam kg
p = float(input('Berat bagasi lebih 110 kg :'))      # berat bagasi lebih dari 110 kg
q = 49                                               # berat bagasi 49 kg

print('Berat bagasi pertama:', p, 'kg', p<=y)
print('Berat bagasi kedua:', q, 'kg', q<=y)
