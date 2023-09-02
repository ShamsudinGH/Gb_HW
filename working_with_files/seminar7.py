import random
from typing import TextIO

# def fill_numbers(file, count_lines):
#     with open(file, 'a', encoding='utf-8') as f:
#         for _ in range(count_lines):
#             f.write(f"{random.randint(-1000, 1000)} | ")
#             f.write(f"{random.uniform(-1000, 1000)} \n")


VOWELS = 'eyuioa'
CONSONANTS = 'qwrtpsdfghjklzxcvbnm'

# def fill_names(file, count_lines):
# #     with open(file, 'a', encoding='utf-8') as f:
# #         for _ in range(count_lines):
# #             lens_name = random.randint(4, 7)
# #             name = ''
# #             for i in range(lens_name):
# #                 if i % 2 == 1:
#                     name += random.choice(VOWELS)
#                 else:
#                     name += random.choice(CONSONANTS)
#             print(name.capitalize(), file=f)


# def read_line_or_begin(fd: TextIO) -> str:
#     text = fd.readline()
#     if text == '':
#         fd.seek(0)
#         text = fd.readline()
#     return text[:-1]


# def convert_files(file_names, file_numbers, files_results):
#     with (open(file_names, 'r', encoding='utf-8') as f_names,
#           open(file_numbers, 'r', encoding='utf-8') as f_numbers,
#           open(files_results, 'w', encoding='utf-8') as fr):
#         len_names = sum(1 for _ in f_names)
#         len_numbers = sum(1 for _ in f_numbers)
#         for i in range(max(len_names, len_numbers)):
#             name = read_line_or_begin(f_names)
#             nums = read_line_or_begin(f_numbers)
#             num_1, num_2 = nums.split('|')
#             res = int(num_1) * float(num_2)
#             if res < 0:
#                 fr.write(f"{name.lower()} {abs(res)} \n")
#             else:
#                 fr.write(f"{name.upper()} {round(res)} \n")

"""Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона."""

import os


def generate_name(min_len_name, max_len_name):
    len_name = random.randint(min_len_name, max_len_name)
    name = ''
    for i in range(len_name):
        if i % 2 == 1:
            name += random.choice(VOWELS)
        else:
            name += random.choice(CONSONANTS)
    return name


def create_files(extension: str, min_len_name: int = 6, max_len_name: int = 30,
                 min_size_file: int = 256, max_size_file: int = 4096, amount_file: int = 42,
                 catalogue_name: str = '') -> None:
    if extension not in os.listdir():
        os.mkdir(catalogue_name)

    for i in range(amount_file):
        filename = generate_name(min_len_name, max_len_name)
        file_size = random.randint(min_size_file, max_size_file)
        data = bytes((random.randint(0, 255)) for _ in range(file_size))
        with open(f"{catalogue_name}/{filename}.{extension}", 'wb') as f:
            f.write(data)


# print(os.listdir())
if __name__ == '__main__':
    #     # fill_numbers('numbers.txt', 200)
    #     # fill_names('names.txt', 70)
    #     # convert_files('names.txt', 'numbers.txt', 'result.txt')
    create_files('txt', catalogue_name='output')
