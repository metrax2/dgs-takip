import os
import requests
from bs4 import BeautifulSoup

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

URL = "https://www.osym.gov.tr/"

def telegram(mesaj):
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": mesaj
        },
        timeout=20
    )

html = requests.get(
    URL,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30
).text

soup = BeautifulSoup(html, "html.parser")
text = soup.get_text(" ", strip=True).lower()

kelimeler = [
    "2027-dgs",
    "dgs başvuru",
    "dgs başvuruları",
    "dikey geçiş sınavı"
]

if any(k in text for k in kelimeler):
    telegram(
        "🔔 DGS BAŞVURU DUYURUSU!\n\n"
        "ÖSYM'de DGS ile ilgili yeni bir duyuru tespit edildi.\n\n"
        "https://www.osym.gov.tr/"
    )
