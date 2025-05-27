import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/catalogue/page-1.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 모든 책 가져오기 (class="product_pod")
books = soup.find_all('article', class_='product_pod')

for book in books:
    # 책 제목은 <h3> 태그 안의 <a> 태그의 title 속성에 있음
    title = book.h3.a['title']

    # 가격은 <p class="price_color">
    price = book.find('p', class_='price_color').text

    # 재고는 <p class="instock availability"> 안의 텍스트
    stock = book.find('p', class_='instock availability').text.strip()

    print(f"{title} | {price} | {stock}")
