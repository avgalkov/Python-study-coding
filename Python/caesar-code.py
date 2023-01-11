# Шифрование текста на русском или английском языке
# по методу Цезаря с указанием сдвига

russian_lowercase = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
russian_uppercase = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
latin_lowercase = 'abcdefghijklmnopqrstuvwxyz'
latin_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
new_index = 0

def shifr():
    s = input('Введите текст для шифрования:  ')
    rotate = int(input('Укажите величину сдвига:  '))
    new_s = ''
    for i in range(len(s)):
        if s[i] in russian_uppercase :
            new_index = russian_uppercase.find(s[i]) + rotate
            if new_index < len(russian_uppercase):
                new_s += russian_uppercase[new_index]
            elif new_index >= len(russian_uppercase):
                new_s += russian_uppercase[new_index - len(russian_uppercase)]

        elif s[i] in russian_lowercase :
            new_index = russian_lowercase.find(s[i]) + rotate
            if new_index < len(russian_lowercase):
                new_s += russian_lowercase[new_index]
            elif new_index >= len(russian_lowercase):
                new_s += russian_lowercase[new_index - len(russian_lowercase)]

        elif s[i] in latin_uppercase :
            new_index = latin_uppercase.find(s[i]) + rotate
            if new_index < len(latin_uppercase):
                new_s += latin_uppercase[new_index]
            elif new_index >= len(latin_uppercase):
                new_s += latin_uppercase[new_index - len(latin_uppercase)]

        elif s[i] in latin_lowercase :
            new_index = latin_lowercase.find(s[i]) + rotate
            if new_index < len(latin_lowercase):
                new_s += latin_lowercase[new_index]
            elif new_index >= len(latin_lowercase):
                new_s += latin_lowercase[new_index - len(latin_lowercase)]
        
        else:
            new_s += s[i]
    return print(new_s)
shifr()