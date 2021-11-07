from bs4 import BeautifulSoup
import requests
import webbrowser

URL = "https://obrazovaka.ru/test/konstanta-gidroliza-tablica.html"
HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 OPR/75.0.3969.285",
}


def parser_html(url=URL):
    answers = []
    rezult = []
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")

    lesson_and_class = soup.find("div", id="breadcrumbs")
    lesson_and_class2 = []
    for item in lesson_and_class: lesson_and_class2.append(item.get_text(strip=True))

    image = soup.find('img', class_="test-image").attrs["src"]
    test_name = soup.find('div', class_="sides__rht").get_text(strip=True)
    title = soup.find('title').get_text(strip=True)
    lesson = lesson_and_class2[2]
    _class = lesson_and_class2[3]
    answer = soup.findAll("span")
    for i in answer:
        if "вопросов" in i.get_text(strip=True):
            answers.append( i.get_text(strip=True))
    answers = answers[0].split()[0]

    return image, test_name, title, lesson, _class,answers

if __name__ == "__main__":
    image, test_name, title, lesson, _class, answers = parser_html()
    test_url = "http://creepertntboom5.pythonanywhere.com/" + f"?result={answers} правильных ответов из {answers}&test_name={test_name}&title={title}&lesson={lesson}&class={_class}&image={image}&answer={answers}&last_hour={'55'}"
    webbrowser.open(test_url)