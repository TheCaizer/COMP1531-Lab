'''
TODO Complete this file by following the instructions in the lab exercise.
'''

integers = [1, 2, 3, 4, 5]
integers.append(6)
total = 0
for i,num in enumerate(integers):
    print(i,num)
    total = total + num
    print(total)
print(sum(integers))