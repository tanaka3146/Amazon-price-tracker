import requests
from bs4 import BeautifulSoup
from smtplib import SMTP
import time



URL = input("enter the URL of the product: ")
comprices=int(input("enter the expected price: "))
EMAIL_ID = input("enter the email address: ")
PASSWORD = input("enter app password: ")

#"boowhkfjgrxhcqrf"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0;Win64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
}

price=""
title=""

while True:
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find(id="productTitle").get_text()
    price_id = soup.find_all("span", class_="a-price-whole")[0].get_text()
    price=price_id.strip().replace(",", "").replace(".", "")
    print(comprices)
    if int(price)<=comprices:
        break
    time.sleep(43200)
    comprices+=200


print("Title: " + title.strip())
print("Price: " + price.strip())

SMTP_SERVER="smtp.gmail.com"
PORT =587

server = SMTP(SMTP_SERVER,PORT)
server.starttls()
server.login(EMAIL_ID,PASSWORD)

subject="price drop!"
body ="current price: "+price+"\n buy link:"+URL
msg=f"subject:{subject}\n\n{body}"
server.sendmail(EMAIL_ID,EMAIL_ID,msg)
server.quit()