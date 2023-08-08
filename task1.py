import os
import random
import string


def create_random_files(quantity: int):
    file_ext = ['txt', 'jpg', 'mov', 'mp3']
    for _ in range(quantity):
        name = ''.join(random.sample(string.ascii_lowercase, 10)) + '.' + random.choice(file_ext)
        with open(name, 'w', encoding='UTF-8') as file:
            file.write(name)


def rename_group(path: str = os.getcwd(),
                 new_name: str = '',
                 count: int = 1,
                 in_ext: str = 'txt',
                 out_ext: str = 'doc',
                 limits: tuple = (0, 10)):
    counter = 1
    if os.path.isdir(path):
        for file in os.listdir(path):
            name, ext = file.rsplit('.', 1)
            if ext == in_ext or not in_ext:
                re_name = f'{name[limits[0]:limits[1]]}{new_name if new_name else ""}{counter:0>{count}}.{out_ext}'
                os.rename(os.path.join(path, file), os.path.join(path, re_name))
                counter += 1
        return f'Было переименовано {counter - 1}'
    else:
        return 'Это не директория!'


#create_random_files(10)
rename_group(new_name='NEW', in_ext='mp3', out_ext='EXE', count=5, limits=(3, 6))
