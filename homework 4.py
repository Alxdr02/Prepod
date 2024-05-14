immutable_var = tuple( (1, 2, 'Bander'))
print(immutable_var)
#immutable_var[0]= 3
#print(immutable_var)# замена в кортеже запрещена, возможно только добавлять элементы
mutable_list=['food', 'beef', 'milk']
mutable_list[0]= 'cucumber'
print(mutable_list)