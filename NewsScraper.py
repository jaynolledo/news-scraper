from GoogleNews import GoogleNews
import pandas as pd

news = GoogleNews(period='1d')
keyword = input('Enter a keyword: ')
news.search(keyword)
result = news.result()

data = pd.DataFrame.from_dict(result)
data = data.drop(columns=["img"])
data.head()

for news in result:
    print("Title : ", news["title"])
    print("News : ", news["desc"])
    print("Read Full News : ", news["link"])
    print()
    