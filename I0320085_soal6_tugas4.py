x = 4  # 4  = 0000 0100
y = 11  # 11 = 0000 1011

z = x | y;
print('Line 1 - Value of z is', z)

z = x >> y;
print('Line 2 - Value of z is', z)

z = x ^ y;
print('Line 3 - Value of z is', z)

z = ~x;
print('Line 4 - Valueof z is', z)

z = y & x;
print('Line 5 - Value of z is', z)
