# Генератор паролей
# Подключаем модуль рандом и объявляем начальные значения
from random import *
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''
# Запрашиваем у пользователя параметры для генерации
print('Укажите количество паролей для генерации')
count_of_pass = int(input())
print('Задайте длину пароля')
length = int(input())
print('Включать ли в пароль цифры?')
with_digits = input('да / нет:  ')
print('Включать ли в пароль прописные буквы?')
with_lower = input('да / нет:  ')
print('Включать ли в пароль заглавные буквы?')
with_upper = input('да / нет:  ')
print('Включать ли в пароль символы ?')
with_punctuation = input('да / нет:  ')
print('Исключать ли неоднозначные символы?')
with_ambiguous = input('да / нет:  ')
if with_digits == 'да':
    chars += digits
if with_lower == 'да':
    chars += lowercase_letters
if with_upper == 'да':
    chars += uppercase_letters
if with_punctuation == 'да':
    chars += punctuation
if with_ambiguous == 'да':
    for s in '':
        if s in 'il1Lo0O':
            chars.replace(s, '')       
# Объявляем функцию генерации в соответствии с введенными ранее параметрами
def generate_password(length_of_password, available_chars):
    for i in range(1, count_of_pass + 1):
        print('Пароль №', i, '   ', ''.join(sample(available_chars,length_of_password)),sep='') 
# Вызываем функцию генерации
generate_password(length, chars)   