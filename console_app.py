from parser_html import  parser_html
import webbrowser

print("History hack")
print("Введите ссылку на тест:")
while True:
    URL = input(">>>")
    try:
        image, test_name, title, lesson, _class, answers = parser_html(URL)
        print("Успешно.")
        print(f"Количество вопросов {answers}. Сколько вы хотите баллов себе?")
        result = input(">>>")
        test_url = "http://creepertntboom5.pythonanywhere.com/" + f"?result={result} правильных ответов из {answers}&test_name={test_name}&title={title}&lesson={lesson}&class={_class}&image={image}&answer={answers}&last_hour={'55'}"
        print("Открывается...")
        webbrowser.open(test_url)

    except:
        print("Возникла Какая-то ошибка")

    finally:
        print("Хотите, можете написать еще одну ссылку")