from bs4 import BeautifulSoup
import requests
import csv

# with open('simple.html') as html_file:
#     soup=BeautifulSoup(html_file,'lxml')

# # print(soup.prettify())
# # print(soup.title.text)
# # match=soup.find('div',class_='footer')
# for article in soup.findAll('div',class_="article"):
# # print(article)
#     headline=article.h2.a.text
#     print(headline)
#     summary=article.p.text
#     print(summary)
#     print()

html_file=requests.get('https://coreyms.com/').text
soup=BeautifulSoup(html_file,'lxml')
csv_file=open('scrape.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(["Headline","Summary","Video-Link"])
# print(soup.prettify())
for article in soup.findAll('article'):
    # print(article.prettify())
    headline=article.h2.a.text
    print(headline)
    summary=article.find('div',class_="entry-content").p.text
    print(summary)
    try:
        video_src=article.find("iframe",class_="youtube-player")["src"]
        # print(video_src)
        vid_id=video_src.split('/')[4]
        vid_id=vid_id.split('?')[0]
        # print(vid_id)
        yt_link=f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link="No Vedio for this post"
       
    print(yt_link)
    print()
    csv_writer.writerow([headline,summary,yt_link])

csv_file.close()