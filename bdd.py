#! /usr/bin/env python
import requests
from bs4 import BeautifulSoup
import logging
import mysql.connector

logging.basicConfig(filename='bdd.log', 
                    level=logging.INFO, 
                    format=f'%(asctime)s - %(name)s - %(threadName)s - %(message)s')
class MyDB():
    def __init__(self):
        Mybdd = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Overlord97.1',
            database='scraptest'

        )

        def insertInBdd(values):
            logging.info('insert into database: start')
            mycursor = mybdd.cursor()
            val = values
            sql = "INSERT INTO articles (title,image,content,date) values (%s,%s,%s,%s);"
            mycursor.execute(sql,val)
            mybdd.commit()
            logging.info('end of insertion')
            return str(mycursor) + "nouvelle entree"
        
        def insertUser(values):
            logging.info('Insert users into database: start')
            curs = mybdd.cursor()
            sql2 = "INSERT INTO users(username,password) VALUES (%s,%s);"
            curs.execute(sql2)
            mybdd.commit()
            logging.info('user add into database')
        

        def getArticle():
            url='https://wikileaks.org'
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            article_main = soup.find_all('li', class_="tile")

            for article in article_main:
                article_title = article.h2.text
                article_img ="http://wikileaks.com" + article.img.attrs['src']
                article_date = article.find('div',class_='timestamp').text
                article_content = article.p.text
                insertInBdd([article_title,article_img,article_content, article_date])

        getArticle()