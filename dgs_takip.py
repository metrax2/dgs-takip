TEST_MODE = True
import os
import requests
from bs4 import BeautifulSoup

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

URL = "https://www.osym.gov.tr/"

# Sadece 2027 DGS ile ilgili ifadeleri takip et
KEYWORDS = [
    "2027-dgs",
    "2027 dgs",
    "2027 dikey geçiş sınavı"
]

html = requests.get(
    URL,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30
).text

soup = BeautifulSoup(html, "html.parser")
text = soup.get_text(" ", strip=True).lower()

found = [k for k in KEYWORDS if k in text]

if TEST_MODE or found:
    message = (
        "🚨🚨 DGS BAŞVURULARI / DUYURUSU! 🚨🚨\n\n"
        "ÖSYM'de 2027 DGS ile ilgili yeni bir içerik tespit edildi.\n\n"
        "ÖSYM:\n"
        "https://www.osym.gov.tr/"
    )

    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": message
        },
        timeout=20
    )
