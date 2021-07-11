import bs4
import requests
from bs4 import BeautifulSoup
import csv
lists = [["Name", "URL", "Author", "Price", "Number of ratings", "Average Rating"]]
a = "https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_pg_"
for i in range(1, 6):
    x = "https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/#"+str(i)+"?ie=UTF8&pg="+str(i)    
    fp = requests.get(x)
    soup = BeautifulSoup(fp.content, 'html.parser')
    for tem in soup.find_all("div", class_="zg_itemImmersion"):
        tag = tem.find_next("div", class_="a-section a-spacing-none p13n-asin")
        name = tag.find_next("a").find_next("div", class_= \
	"p13n-sc-truncate").string.strip()
        pric = tag.find_next("a", class_= \
	"a-link-normal a-text-normal").span.span.string
        rating = tag.find_next("div", class_= \
	"a-icon-row a-spacing-none").a.text.replace("\n", "").strip()
        url = "https://www.amazon.com"+tag.a["href"].replace("\n", "").strip()
        votes = tag.find_next("div", class_="a-icon-row a-spacing-none"). \
        find_next("a", class_= \
	"a-size-small a-link-normal").string.replace("\n", "").strip().replace(",", "")
        votes = int(votes)
        author = tag.find_next("div", class_="a-row a-size-small").span
        if author is None:
            author = tag.find_next("div", class_="a-row a-size-small"). \
            find_next("a", class_="a-size-small a-link-child").string
        else:
            author = author.string
        list1 = [name, url, author, pric, votes, rating]
        lists.append(list1)
with open('output/com_book.csv', 'w', newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(lists)
