'''
listExample = [
    'ular',
    42,
    3.9,
    True,
    50
]
'''

'''
print(listExample[0])
print(listExample[1:4])
print(listExample[-1])
print(listExample)
'''

# List Command

'''
# akan insert ke urutan 1
listExample.insert(1, 'Database')
print(listExample)

# masukin di belakang
listExample.append("Matamu")
print(listExample)
'''

# remove, pop, clear, del

# listExample.remove('ular')
# print(listExample)

# hilangkan index terakhir
# listExample.pop()
# print(listExample)

#  delete index tertentu
# del listExample[2]
# print(listExample)

# hilangkan semua list
# listExample.clear()
# print(listExample)



# Iterations untuk list
# listExample = [
    # 40, 50, 20, 70, 80
    # 40, 55, 20, 75 , 80
# ]

# for item in listExample:
#     print(item)

# for item in listExample:
#     if item % 2 == 0:
#         print(item)

# if 40 in listExample:
#     print("ada tuh angka 40")


# listExample = [40, 55, 20, 75, 80]
# listExample2 = listExample
# listExample2 = listExample.copy()
# listExample2[0] = 100

# print(listExample)
# print(listExample2)


# listExample = [40, 55, 20]
# listExample2 = [70, 100]

# Digabungkan antara 2 list
# print(listExample + listExample2)

# listExample.extend(listExample2)
# print(listExample)


# listExample = [40, 55, 20]
# print(listExample.index(55))

# listExample = [40, 55, 20]

# listExample.sort()

# print(listExample)


listExample = [40, 55, 20]

listExample.reverse()

print(listExample)