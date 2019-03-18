def foo(a: int, b: int) -> int:
    """
    Тест документации
    """
    # все что после ":" в аргументе функции, то ожидаемый параметр.  После "->" ожидаемый return
    return a + b


# print(foo.__annotations__) #список всех типов аргументов
# print(foo.__doc__) #вывод документации функции

f = foo(1, 3)


def multylier_factory (n):
    def multylier(m):
         return n * m
    return multylier

# или с помощью lambda
def multylier_factory (n):
    return lambda m: n * m


x10 = multylier_factory(10)
print(x10(5))

# =====================================

multilist = [multylier_factory(x) for x in range(20)]

for i in multilist:
    print(i(10))

# или

print(multilist[4](10)) # Обращаемся к 4й ячейки функции, где происходит умножение на 4

def foo2 (a, b=14, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
    print(f'locals^ {locals()}')

foo2(1, 2, 3, 4, 5, 6, c=7, d=8, e=9)


# Распаковка
a, b, c, *d = (1, 2, 3, 4, 5, 6, 7, 8) # *- все остальное
print(a)
print(b)
print(c)
print(d)


# lambda
print(lambda x, y: (x * y)(1, 2))
print(sorted({5: 'a', 3: 'b', 0: 'c'}.items(), key=lambda x:x[1]))


# Сортировка
x = [(1, 'a'), (10, 'h'), (14, 'b')]
x.sort(key=lambda tup: tup[1]) # sort - возвращает отсортированный массив
print(x)
x2 = sorted(x, key=lambda tup: tup[1]) #sorted - возвращает копию отсортированного массива
print(x2)

