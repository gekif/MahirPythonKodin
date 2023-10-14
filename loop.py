'''
for i in range(6):
    print("Looping")
'''


'''
range(0, 8, 2)
0: awal 
8: akhir 
2: plus 2 -> tidak wajib ada
'''
'''
# for i in range(0, 8, 2):
for i in range(0, 10):
    print(i)
'''

'''
# Break and continue
for i in range(10, 20, 3):
    if i == 19:
        break
    print(i)
'''

# Print angka ganjil 1 sampai  10
'''
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
'''

'''
# sama dengan diatas
for i in range(1, 11):
    if i % 2 != 0:
        print(i)
'''


# While Statement
'''
nilai = 50

while (nilai < 70):
    print("Nilai Sekarang:", nilai)
    nilai +=5
'''

uang = 100

while (uang > 0):
    print("Masih punya uang:", uang)
    uang -= 10

print("Uang sudah habis")