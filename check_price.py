import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.in/SARGE-Metal-LED-Surface-Light/dp/B01DBGT1IQ/ref=sr_1_1?keywords=sar+green+energies&qid=1566643925&s=gateway&sr=8-1'

headers = {"User-agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

def check_price():
	page = requests.get(URL, headers=headers)

	soup = BeautifulSoup(page.content, "html.parser")

	title = soup.find(id="productTitle").get_text()
	print(title.strip())

	price = soup.find('span', {'class':"a-color-price"}).get_text()
	price = price.replace('₹', '')
	print(price)
	converted_price = price[0:5]
	print(converted_price)

	if(converted_price < 700):
		send_mail()

def send_mail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('athena.saurav@gmail.com', 'gtwjdcxpjqjoimwf')

	subject = 'Price over 700'
	body = 'check the amazon link https://www.amazon.in/SARGE-Metal-LED-Surface-Light/dp/B01DBGT1IQ/ref=sr_1_1?keywords=sar+green+energies&qid=1566643925&s=gateway&sr=8-1

	msg = f"subject: {subject}\n\n{body}"
	server.sendmail(
		'athena.saurav@gmail.com'
		'techperitia@gmail.com'
		msg
	)
	print('Hey Email Sent')

	server.quit()

check_price()





