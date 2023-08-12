#!/usr/bin/python3.10
my_dict={'fruit': 'apple', 'animal': 'fox', 1:'one', 'two': 2 }
my_dict.pop('two')
print(my_dict)
removed_item=my_dict.popitem()
print(my_dict)
print(removed_item)
