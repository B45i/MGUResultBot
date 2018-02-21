from bs4 import BeautifulSoup
import requests
from config import token, chat_id


TELEGRAM_API = 'https://api.telegram.org/bot' + token
MGU_URL = 'http://projects.mgu.ac.in/bTech/btechresult/index.php?module=public&attrib=result&page=result'

def send_message(text):
    data = {'chat_id': chat_id, 'text': text}
    response = requests.post(TELEGRAM_API + '/sendMessage', data=data)
    print response.content

def main():

if __name__ == '__main__':
    main()