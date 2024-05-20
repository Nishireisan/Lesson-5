# food = ['fdsf', 'fdfsada']
# print(food)
# print(type(food))
# dast = food, 1, 2, 3
# print(dast)
# print(type(dast))
immutable_var = 1, 1.25, "еда", 1 < 6
print(immutable_var)
#immutable_var[1] = 4
print(immutable_var) #в кортеже нельзя изминить содержимое, если это не список
mutable_list = [1, 3, 6, 89, 'svekla']
print(mutable_list)
mutable_list[4] = 'carrot'
print(mutable_list)
