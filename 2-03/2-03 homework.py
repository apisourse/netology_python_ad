from datetime import datetime
import os


def save_log(func):

    def write_somefunc_parametrs(*args, **kwargs):
        function_start = datetime.today()
        function_name = func.__name__
        function_args = args
        global function_result
        function_result = func(*args, **kwargs)
        log_string = 'Func_start: {a}, Func_name: {b}, Func_arg: {c}, Func_result:{d}\n'.format(
            a=function_start, b=function_name, c=function_args, d=function_result)
        file_name = 'log.txt'
        with open(file_name, 'a', encoding='utf-8') as f:
                f.writelines(log_string)
        print('log:', os.getcwd()+'/'+file_name)

        return function_result
    return write_somefunc_parametrs


a = 'one_argument'
b = 'two_argument'


@save_log
def some_func(a, b):
    export = '>>> This is some function whis some arguments'
    return export


print(some_func(a, b))
