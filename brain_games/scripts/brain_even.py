import prompt                                                                            #импортируем модуль
import random                                                                            #импортируем модуль random с библиотекой randint
from brain_games.scripts.brain_games import main                                         #обращаемся к импортированной функции main для того, чтобы взять имя ползователя. пригодится в дальнейшем коде.

                                                                                        #функция проверки числа на четность
def is_even(number):
    return number % 2 == 0

                                                                                        #функция описывающая основную логику игры
def brain_even():
    name = main()                                                                       #обращаемся к импортированной функции. для того, чтобы взять имя ползователя. пригодится в дальнейшем коде.
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    answer_count = 0                                                                    #счетчик правильных ответов. при правильном ответе добавляем 1.
    
    for _ in range(3):                                                                  #используем цикл для трех итераций вопросов-ответов

        number = random.randint(1, 10)                                                  #по умолчанию задаем интервалы выборки случайных чисел (от 1 до 10).
        print(f'Question: {number}')
    
        answer = prompt.string('Your answer: ')
        
                                                                                        #прописываем условия\логику правильных или неправильных ответов. используем функцию-предикат is_even().
        if is_even(number) is True and answer == "yes":
            print('Correct!')
            answer_count += 1
        elif is_even(number) is not True and answer == "no":
            print('Correct!')
            answer_count += 1
        elif is_even(number) is not True and answer != "no":
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break                                                                       #при неправильном ответе прерываем выполнение цикла\игры.
        elif is_even(number) is True and answer != "yes":
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {name}!")
            break                                                                       #при неправильном ответе прерываем выполнение цикла\игры.
    if answer_count == 3:                                                               #при достижении трех правильных ответов выводим Поздравление.
        print(f"Congratulations, {name}!")


brain_even()