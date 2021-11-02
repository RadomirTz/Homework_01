from bs4 import BeautifulSoup
import requests


resp_1 = requests.get('https://habr.com/ru/top/daily/page1')
resp_2 = requests.get('https://habr.com/ru/top/daily/page2')
resp_3 = requests.get('https://habr.com/ru/top/daily/page3')


soup_1 = BeautifulSoup(resp_1.text, 'lxml')
soup_2 = BeautifulSoup(resp_2.text, 'lxml')
soup_3 = BeautifulSoup(resp_3.text, 'lxml')


posts_1 = soup_1.findAll('a', class_='tm-article-snippet__title-link')
posts_2 = soup_2.findAll('a', class_='tm-article-snippet__title-link')
posts_3 = soup_3.findAll('a', class_='tm-article-snippet__title-link')


print('Первая страница:')
for post in posts_1:
    print("     Пост: " + post.text)

print('Вторая страница:')
for post in posts_2:
    print('     Пост: ' + post.text)

print('Третья страница:')
for post in posts_3:
    print('     Пост: ' + post.text)