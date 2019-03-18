# Пример 1
list_x = [1, 2, 3]
iter_x = list_x.__iter__()

# print(iter_x) # Смотрим что за зверь
# print(dir(iter_x)) # Показывает методы класса

next_elem = iter_x.__next__()
print(next_elem) # 1
next_elem = iter_x.__next__()
print(next_elem) # 2
next_elem = iter_x.__next__()
print(next_elem) # 3
next_elem = iter_x.__next__()
print(next_elem) # StopIteration


# Пример 2
import string
chars = string.ascii_letters

class ChangeCase:
    def __init__(self, chars: string):
        self.chars = chars
        self.start = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.start += 1
        if self.start != len(self.chars):
            return self.chars[self.start].upper()
        else:
            raise StopIteration

for c in ChangeCase(chars):
    print(c)


# Пример 3
def my_generator():
    while True:
        yield 1

x = my_generator()

for item in x:
    print(item) # Выдаст бесконечные единицы


# Пример 4
# Фибаначи

f = [0, 1, 1, 2, 3, 5, 8]

def fib(n):
    first = 0
    second = 1
    for _ in range(n): # _ Если не нужны итерируемые объекты
        yield first
        third = first + second
        first = second
        second = third

for item in fib(10):
    print(item)


# Пример 5 # map
def sq(x):
    return x * x
list1 = list(range(1, 100))
sq_list = map(sq, list1)
for item in sq_list:
    print(item)

# или

list1 = list(range(1, 100))
sq_list = map(lambda x: x*x, list1)
for item in sq_list:
    print(item)


# Пример 6 # filter # отфильтровывает по условию
list1 = list(range(1, 100))

numbers = list(filter(lambda x: x % 2 == 0, list1))
print(numbers)






# import wikipedia
# wikipedia.set_lang("en")
# search = wikipedia.page("Barack")
# print(search.url)