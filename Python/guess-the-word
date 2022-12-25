from random import choice
word_list = ['mother', 'father', 'sister', 'brother', 'cat', 'brainstorm', 
             'elevator', 'oxygen', 'between', 'language', 'agenda',
             'winter', 'soccer', 'basketball', 'electricity', 'elephant',
             'november', 'october', 'pinapple', 'table', 'philosophy',
             'snowboard', 'leopard', 'rabbit', 'pancake', 'facebook']
def get_word():
    return choice(word_list).upper()

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]
word = get_word()
word_completion = '_' * len(word)

# s1 = list(word_completion)

def play():
    word = get_word()                  #слово
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток
    s1 = list(word_completion)
    print('Давайте играть в угадайку слов!')
    print('Если не угадаете, то Саня повесится, виселица готова') 
    print()    
    print('Угадай слово: ', word_completion, sep=' ') #зашифрованное
    print()
    print(display_hangman(tries))

    while True:
        text = input('Введите слово или букву:').upper()
        if text.isalpha():
            if text != word and len(text) > 1:
                tries -= 1
                guessed_words.append(text)
                print('Попробуйте еще раз!', display_hangman(tries))
                print('Осталось', tries, 'попыток')
                print('Названные слова: ', *guessed_words)
            elif text == word:
                print()
                print('Вы угадали, было загадано слово:', word)
                print('Затрачено попыток:', 6 - tries)
                break
            elif len(text) == 1:


                if text in word:
                    if text in guessed_letters:
                        print('Буква уже была введена')
                        print('Названные буквы', *guessed_letters)
                        continue
                    else:
                        guessed_letters.append(text)
                        tries -= 1                    
                        for i in range(len(word)):           
                            if word[i] == text:                       
                                s1[i] = text                                           
                        print('Вы угадали букву', text)
                        print(display_hangman(tries))
                if text not in word:
                    guessed_letters.append(text)

                    tries -= 1                    
                    print('Такой буквы в слове нет, попробуйте еще раз')
            print('Текушее решение', *s1)
            print('Буквы, которые вы называли', *guessed_letters)
            print('Слова, которые вы называли', *guessed_words)
            print('Осталось', tries, 'попыток')
            print()
        elif  not text.isalpha():
            print('Не верно введен символ!')
        if tries == 0:
            print('К сожалению, вы не угадали слово. Это было слово: ', word)
            print()
            print('Саню жаль конечно, вы во всем виноваты!')
            print()
            print(display_hangman(tries))
            break
        if word_completion == word:
            print('Поздравляем, вы угадали слово! Вы победили!')
            print()
            break
play()
while True:
    print('Может еще разок?')
    print()
    otvet = input('Введите да или нет: ')
    print()
    if otvet in "да":
        word = get_word()
        word_completion = '_' * len(word)
        s1 = list(word_completion)
        play()
        print()
    elif otvet in "нет":
        print('До встречи')
        break
    else:
        print('Не понимаю что вы от меня хотите, введите еще раз')
