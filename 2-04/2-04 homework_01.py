import textwrap

str = 'Какой_то_текст'


def adv_print(*args, **kwargs):
    """
    Descriptions:

    function adv_print(input_text, pre_string, max_width_line, write_to_file)

    input_text - some string text
    pre_string - first line text
    max_width_line - max width text in line
    write_to_file - if True or 'Yes' or 'Да' or 'Y', the formatted text will be written to the 'log.txt'
    """

    start = kwargs.get('start', '\n')
    max_line = kwargs.get('max_line', 100)
    sep = kwargs.get('sep', '')
    if max_line > 100:
        max_line = 100
    in_file = kwargs.get('in_file', True)
    t = sep.join(args)
    text = textwrap.fill(start + t, width=max_line)
    print(text)

    if in_file in [True, 'Yes', 'Да', 'Y']:
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.writelines(text)
    else:
        pass


# >>>>> Чекаем:
# adv_print(str, 'text1', 'text2', start='Итоги: ', max_line=50, in_file=True, sep=' ')
# adv_print(str, 'text2', start='Итоги: ', max_line=50, in_file=True, sep=' ')
adv_print(str, 1, 'text2', sep='========')
