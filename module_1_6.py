#2
my_dict = {'Vadim': 2000, 'Ivan': 1998, 'Oleg': 2001}
print(my_dict)
print(my_dict.get('Vadim'))
print(my_dict.get('Dima'))
my_dict.update({'Vlad': 2002, 'Egor': 1999,})
I = my_dict.pop('Ivan')
print(I)
print(my_dict)

#3
my_set = {'Apple', 1, 12.5, 1, 3, 'Pineapple', 'Apple', 2, 13.4, 13.4}
print(my_set)
my_set.add((5, 6, 7))
my_set.add('Banana')
my_set.remove(13.4)
print(my_set)