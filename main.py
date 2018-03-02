import requests
import time
from bs4 import BeautifulSoup
from config import token, chat_id


TELEGRAM_API = 'https://api.telegram.org/bot' + token
MGU_URL = 'http://projects.mgu.ac.in/bTech/btechresult/index.php?module=public&attrib=result&page=result'
interval = 10 # Time interval in minutes

def send_message(text):
    data = {'chat_id': chat_id, 'text': text}
    response = requests.post(TELEGRAM_API + '/sendMessage', data=data)
    print response
    # print response.content

def check_result():
    while(True):
        page = requests.get(MGU_URL)
        soup = BeautifulSoup(page.text, 'html.parser')
        exams = str(soup.findAll('option'))

        prev_file = open('previous.txt', 'r')
        prev_exams = prev_file.read()
        prev_file.close()
        
        if prev_exams != exams:
            msg_str = 'Results for :\n'
            for list in soup.findAll('option')[1:]:
                msg_str += list.contents[0] + ',\n'
            msg_str += 'are now avilable on ' + MGU_URL
            send_message(msg_str)

            file = open('previous.txt', 'w')
            file.write(exams)
            file.close()
        time.sleep(interval*60)

def main():
    check_result()

if __name__ == '__main__':
    main()
