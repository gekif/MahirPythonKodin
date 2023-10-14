tupleExample = (
    'Ular', 20, 3.8, True, 20
)

# [] -> List
# () -> Tuple
# {} -> Dictionary

# print(tupleExample)


# Dictionary (Key Value)

'''
customer = {
    "nama" : "Ceby",
    "umur" : 25
}

customer["pekerjaan"] = "tukang parkir"
customer.pop("umur")

print(customer)

# print(customer["nama"])
# print(customer["umur"])
'''


#  Set
numbers1 = {1, 3, 4, 5, 10}
numbers2 = {3, 4, 10, 7, 8}

# numbers_union = numbers1.union(numbers2)
# print(numbers_union)

# difference1 = numbers1.difference(numbers2)
# print(difference1)

# sym_difference =  numbers1.symmetric_difference(numbers2)
# print(sym_difference)

intersect = numbers1.intersection(numbers2)
print(intersect)