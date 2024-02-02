from bs4 import BeautifulSoup
import requests
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

bot_token = "6710454348:AAH29KcinmIeH7yPDyN8IbOhgbHI92238lQ"
chat_id = "748894930"

response = requests.get('https://www.bbc.com/amharic')
soup = BeautifulSoup(response.text, 'html.parser')
titles = soup.find_all('div', class_='promo-text')
descriptions = soup.find_all('p', class_='promo-paragraph bbc-1un1asj ewjbyra0')
links = soup.find_all('a', class_='focusIndicatorDisplayBlock bbc-uk8dsi e1d658bg0')

def send_to_telegram(bot_token, chat_id, text):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(url, params=params)
    return response.json()

for index, entry in enumerate(titles):
    title = entry.get_text(strip=True)
    description = descriptions[index].get_text(strip=True)
    
    link = links[index]['href']
    
    texts = f"Title: {title}\nDescription: {description}\nLink: {link}\n"
    response = send_to_telegram(bot_token, chat_id, texts)
    print(response)
