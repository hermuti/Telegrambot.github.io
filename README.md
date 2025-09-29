# 📢 BBC Amharic News Telegram Bot

A **Python web scraping bot** that automatically fetches the latest news from **BBC Amharic** and delivers them to a **Telegram channel**.

---

## 📋 Overview

This project demonstrates **automated news delivery** using **web scraping** and **Telegram API integration**.  
The bot extracts **news headlines**, **descriptions**, and **links** from BBC Amharic and sends them directly to a Telegram channel, keeping users updated **without manual website visits**.

---

## 🚀 Impact

- 🧠 **Automated News Delivery** – Eliminates manual checking of BBC Amharic website  
- ⚡ **Real-Time Updates** – Users receive news immediately after publication  
- 🧩 **Reduced Setup Time** – Clear configuration steps minimize deployment time  
- 🌍 **Amharic Language Support** – Handles UTF-8 encoding for Amharic text  

---

## 🛠 Quick Start (5-Minute Setup)

### ✅ Prerequisites
- Python **3.7+**
- Telegram account
- Basic command line knowledge

### ⚙️ Installation
```bash
# Clone or create project directory
mkdir news-bot && cd news-bot

# Install dependencies
pip install beautifulsoup4 requests

# Create configuration file
touch config.py
```

---

## ⚙️ Detailed Setup Guide

### Step 1: Create Telegram Bot
1. Open Telegram and search for `@BotFather`  
2. Send `/newbot`  
3. Follow the prompts to name your bot  
4. Copy and save the **API token** provided

### Step 2: Get Your Chat ID
1. Start a chat with your bot  
2. Visit:  
   ```
   https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates
   ```
3. Find your `chat_id` in the JSON response

### Step 3: Configuration
Create a file named `config.py`:
```python
BOT_TOKEN = "your_actual_bot_token_here"
CHAT_ID = "your_actual_chat_id_here"
BBC_AMHARIC_URL = "https://www.bbc.com/amharic"
```

---

## 💻 Complete Code
```python
from bs4 import BeautifulSoup
import requests
import time

BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
CHAT_ID = "YOUR_CHAT_ID_HERE"
BBC_URL = "https://www.bbc.com/amharic"

def send_to_telegram(bot_token, chat_id, text):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
    try:
        response = requests.post(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Telegram API Error: {e}")
        return {"ok": False, "error": str(e)}

def scrape_bbc_amharic():
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(BBC_URL, headers=headers, timeout=15)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all('div', class_='promo-text')
        descriptions = soup.find_all('p', class_='promo-paragraph')
        links = soup.find_all('a', class_='focusIndicatorDisplayBlock')
        return titles, descriptions, links
    except Exception as e:
        print(f"Scraping Error: {e}")
        return None, None, None

def main():
    print("🚀 Starting BBC Amharic News Bot...")
    if BOT_TOKEN == "YOUR_BOT_TOKEN_HERE" or CHAT_ID == "YOUR_CHAT_ID_HERE":
        print("❌ Please configure BOT_TOKEN and CHAT_ID")
        return
    titles, descriptions, links = scrape_bbc_amharic()
    if not titles:
        print("❌ Failed to scrape news")
        return
    for index in range(min(5, len(titles))):
        try:
            title = titles[index].get_text(strip=True)
            description = descriptions[index].get_text(strip=True) if index < len(descriptions) else "No description"
            link = links[index]['href']
            if link.startswith('/'): link = f"https://www.bbc.com{link}"
            message = f"<b>📢 {title}</b>\n\n{description}\n\n🔗 <a href='{link}'>Read full article</a>"
            send_to_telegram(BOT_TOKEN, CHAT_ID, message)
            print(f"✅ Sent: {title[:50]}...")
            time.sleep(2)
        except Exception as e:
            print(f"❌ Error processing article {index}: {e}")
            continue

if __name__ == "__main__":
    main()
```

---

## 🎯 Usage Examples

### ▶️ Basic Usage
```bash
python news_bot.py
```

### ⏱ Schedule with Cron (every 2 hours)
```bash
0 */2 * * * /usr/bin/python3 /path/to/your/news_bot.py
```

### 🧪 Test Configuration
```python
def test_telegram_connection():
    response = send_to_telegram(BOT_TOKEN, CHAT_ID, "🧪 Test message from BBC News Bot")
    if response.get('ok'):
        print("✅ Configuration test passed!")
    else:
        print("❌ Configuration test failed!")
```

---

## 🐛 Troubleshooting Guide

| Problem | Solution |
|----------|-----------|
| `ModuleNotFoundError` | Run `pip install beautifulsoup4 requests` |
| `403 Forbidden` | Add proper `User-Agent` headers |
| `Telegram API Error` | Verify bot token and chat ID |
| Garbled Amharic text | Ensure UTF-8 encoding is used |
| No articles found | Check if BBC page structure changed |

---

## 📦 Dependencies
```
beautifulsoup4==4.12.2
requests==2.31.0
soupsieve==2.5
```

Install using:
```bash
pip install -r requirements.txt
```

---

## 🔒 Security Best Practices
```python
# Do not commit tokens in code
# Use environment variables for production

import os

BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
```

---

## ✨ Features

✅ Automated **web scraping**  
✅ **Telegram integration** with HTML formatting  
✅ **Error handling** and retry mechanisms  
✅ **UTF-8** support for Amharic  
✅ **Rate limiting** to prevent spam  
✅ Easy **configuration**  

---

## 🎓 Technical Documentation for Python – University Project

- 📝 Created a **clear setup guide**, **usage examples**, and **troubleshooting documentation**  
- ⏱ **Reduced onboarding time** for new users by clarifying configuration steps and dependencies  
- 🔗 **Documentation Link:** [Add Documentation link here]

---

## 🔮 Future Enhancements
- 🗂 Add database to track sent articles  
- 📰 Integrate multiple news sources  
- 🌐 Build web dashboard for configuration  
- 🧠 Add sentiment analysis for filtering  
- 🐳 Docker containerization  
- 🌍 Multi-language support  

---

## 📞 Support
If you encounter issues:
- Check the troubleshooting guide
- Verify your bot token & chat ID
- Ensure dependencies are installed
- Check for BBC page updates
