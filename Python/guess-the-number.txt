# Числовая угадайка
from random import randint
print('Добро пожаловать в числовую угадайку')
def is_valid(n):
    if n.isdigit():
        if 1 <= int(n) <= 100:
            if str(int(n)) == n:
                return True
    else:        
        return False
def game():
    num = randint(1,100)
    counter = 0            
    while True:
        print("Введите число от 1 до 100")
        n1 = input()
        counter += 1
        if is_valid(n1) == True:
            if int(n1) < num:
                print('Ваше число меньше загаданного, попробуйте еще разок')
            
            elif int(n1) > num:
                print('Ваше число больше загаданного, попробуйте еще разок')
                
            elif int(n1) == num:
                print('Вам потребовалось', counter, 'попыток, поздравляем')
                break
        else:
            print("А может быть все-таки введем целое число от 1 до 100?")
game()
print('Если хотите сыграть еще раз, напишите "да"')
if input() != 'да':
    print('Goodbye')        
else:
    game()