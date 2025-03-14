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

#Lets Send the email

print('Composing the Email...')

# update your email details
SERVER = 'smtp.gmail.com' # AS our smtp server
PORT = '587' #port number
FROM = 'zamad.shakeel.01@gmail.com' #your email
TO = 'zamad.shakeel.01@gmail.com' #reciever email
PASS = 'Pakistan5050.'

Server = smtplib.SMTP(SERVER, PORT)
Server.set_debuglevel(1)
Server.ehlo()
Server.starttls()
Server.login(FROM, PASS)
Server.sendmail(FROM, TO, content.as_string())

print('Email Sent...')
Server.quit()





