#test
print("Привет!Ты попал на мой тест.Если ты его пройдешь,то в конце тебя ждет сюрприз.")
print("Ответы вводить в буквах на русском языке.")
def vopros(pravilniy,pravilniy2,pravvopros,variant):
    score = int(0)
    print(pravvopros)
    print(variant)
    answer = str(pravilniy)
    answer2 = str(pravilniy2)
    otvet = str(input())
    if answer == otvet or answer2 == otvet:
        score = score + 1
        print("Правильный ответ!")
        print("Следующий вопрос.")
    else:
        print("Ответ неверный.Следующий вопрос!")
    return
vopros("ответ с маленькой буквы","ответ с большой буквы","сам вопрос ","варианты ответа")