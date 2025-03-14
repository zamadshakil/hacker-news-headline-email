import requests #for http requests
from bs4 import BeautifulSoup #for web scraping 

#for email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#for date and time
import datetime
now = datetime.datetime.now() #current date and time

#for email sending 
import smtplib

content = ''

#func. to get Hacker News Stories
def getNews(url):
    print('Extracting the Hacker News Stories...')
    cnt = ''
    cnt += ('<b>Headline Stories : </b>' + '<br>' + '-'*50 + '<br>')
    response = requests.get(url)
    content = response.content
    HTML = BeautifulSoup(content, 'html.parser')

    for i, tag in enumerate(HTML.findAll('td', attrs = {'class':'title', 'valign' : ''})):
        cnt += ((str(i+1) + ' :: ' + tag.text + "\n" +'<br>') if tag.text!='More' else '')
        return cnt

#Getting the News Content
rawContent = getNews('https://news.ycombinator.com/')
content += rawContent
content += ('<br>------<br><br>End of Message!')





