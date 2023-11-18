from bs4 import BeautifulSoup
import requests
import os

def save_to(file_name, mode, data):
    with open(file_name, mode, encoding='utf-8') as file:
        file.write(data+'\n')

def log(msg):
    print('[+]', msg)

def crawl_url(url):
    log('getting response')
    response = requests.get(url)
    save_to('response.html', 'w', response.text)
    log('response saved to reaponse.txt')

    log('creating soup')
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.find_all('h3')
    for ele in data:
        log(ele)
        save_to('soup.txt', 'a', ele.text)
    # log('soup saved to soup.txt')

    log('done')

if __name__ == "__main__":
    # crawl_url('https://stackoverflow.com/questions/73871708/telebot-python-and-inlinekeyboard')
    crawl_url('https://www.google.com/search?q=beautiful+soup&oq=beautiful+soup&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDQ4NzNqMGoxqAIAsAIA&sourceid=chrome&ie=UTF-8')


