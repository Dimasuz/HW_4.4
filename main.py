print('Задание 1. Написать итератор, который принимает список списков, и возвращает их плоское представление, т.е последовательность состоящую из вложенных элементов.')

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]


class FlatIterator:
  
  def __init__(self, list_of_list):
    self.list_of_list = [x for l in list_of_list for x in l]
          
  def __iter__(self):    
    self.cursor = 0
    return self

  def __next__(self):
    self.cursor += 1    
    if self.cursor == len(self.list_of_list) + 1:
      raise StopIteration
    else:
      return self.list_of_list[self.cursor - 1]

for item in FlatIterator(nested_list):
  print(item)

print()
print('Задание 2. Написать генератор, который принимает список списков, и возвращает их плоское представление.')


def flat_generator(list_of_list):
  list_of_list = [x for l in list_of_list for x in l]
  start = 0
  while start < len(list_of_list):
    yield list_of_list[start]    
    start += 1
    
for item in  flat_generator(nested_list):
  print(item)
