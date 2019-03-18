import random
import string
import hashlib
import datetime


def hash_parametrized_decorator(hash_format):

    def hash_decorator(old_func):
        hash_list = []
        count = 0

        def new_func(*args, **kwargs):
            password = old_func(*args, **kwargs)
            hashfunc = hash_format()
            hashfunc.update(password.encode())
            digest = hashfunc.digest()
            hash_list.append(digest)
            print(hash_list)

            nonlocal count
            count += 1
            print(count)

            return digest
        return new_func
    return hash_decorator


def time_inspector(input_func):
    def inspector_func(*args, **kwargs):
        starttime = datetime.datetime.now()
        func = input_func
        endtime = datetime.datetime.now()
        print(endtime - starttime)
        return func
    return inspector_func


@ hash_parametrized_decorator(hashlib.sha256)
# @time_inspector
def generate_pass(n):
	password = list()
	chars = string.ascii_letters
	for _ in range(n):
		password.append(random.choice(chars))  # случайное рандомное число
	return ''.join(password)


print(generate_pass(10))
print(generate_pass(10))
print(generate_pass(10))
