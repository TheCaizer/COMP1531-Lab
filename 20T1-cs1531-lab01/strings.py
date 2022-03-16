'''
TODO Complete this file by following the instructions in the lab exercise.
'''

strings = ['This', 'list', 'is', 'now', 'all', 'together']
ns = ''
for n in strings:
    ns += n + " "
print(ns[:-1])
print(' '.join(strings))