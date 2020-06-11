import requests
from bs4 import BeautifulSoup
import datetime
import json

def get_href(url, today, articles):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    results = soup.select("div.title")
    date = soup.select("div.date")
    tTweet = soup.select("div.nrec")
    aAuthor = soup.select("div.author")
    isToday = today  #用於紀錄這一頁的非今日日期 先初始化為今日
    
    for title, whatday, tweet, author  in zip(results, date, tTweet, aAuthor):
        temp_url = title.select_one("a") #<a href="">中的網址
              
        if temp_url:
            temp_url = 'https://www.ptt.cc'+ temp_url.get('href')
            temp_date = whatday.text #發文日期
            temp_title = title.find("a").text
            #temp_title = title.text  #標題
            temp_author = author.text  #作者
            
            if tweet.select_one("span"):
                temp = tweet.select_one("span").text  #推文數
            
                try:
                    temp_tweet = int(temp)
                except ValueError:
                    if temp == '爆':
                        temp_tweet = 99
                    elif temp.startswith('X'):
                        temp_tweet = -10            
            else:
                temp_tweet = 0
            
            #print(temp_date)
            if temp_date == today:    
                articles.append({
                    "title":temp_title, "href":temp_url, "tweet":temp_tweet, "author":temp_author})
                #print(temp_title, 'https://www.ptt.cc'+ temp_url.get('href'), temp_author,temp_tweet)
                
            # 符合條件
            else:
                if url != "https://www.ptt.cc/bbs/C_Chat/index.html":  #第一頁有置頂文不算
                    isToday = temp_date  #不是今日發的文 把日期更改為非今日的日期
    
    return isToday
     

def save_to_json(articles, file):
    print("今天共有：", len(articles), "篇文章")
    
    with open(file, "w", encoding = "utf-8") as fp:
        json.dump(articles, fp, indent = 2, sort_keys = True, ensure_ascii = False)  #寫檔

    json_articles = json.dumps(articles)  # list to json
    return json_articles

def get_ptt(isToday, today, url, articles):
    while isToday == today:  #如果文章還是在今日發的
        r = requests.get(url)
        soup = BeautifulSoup(r.text,"html.parser")
        btn = soup.select('div.btn-group > a') #找到換頁區的按鈕
        up_page_href = btn[3]['href'] #上一頁是在第四個標籤
        next_page_url = 'https://www.ptt.cc' + up_page_href
    
        isToday = get_href(url, today, articles)  #每次都會回傳日期
        url = next_page_url #上一頁

    articles = sorted(articles, key = lambda k: k["tweet"], reverse = True)  #對tweet做排序
    #for item in articles:
    #print(articles[0])
    #print(articles[1])
    #print(articles[2])

    return save_to_json(articles, "articles.json")
  

def run():
    #將日期改為01 02 ... 這種
    if datetime.date.today().day < 10:
        if datetime.date.today().month < 10:
            today = ' ' + str(datetime.date.today().month) + "/" + '0' + str(datetime.date.today().day)
        else:
            today = str(datetime.date.today().month) + "/" + '0' + str(datetime.date.today().day)
    else:
        if datetime.date.today().month < 10:
            today = ' ' + str(datetime.date.today().month) + "/" + str(datetime.date.today().day)
        else:
            today = str(datetime.date.today().month) + "/" + str(datetime.date.today().day)

    url="https://www.ptt.cc/bbs/C_Chat/index.html"
    isToday = today #是否為今天的文
    articles = [] 
    #return get_ptt(isToday, today, url, articles)
    get_ptt(isToday, today, url, articles)
    return articles