from requests_html import HTMLSession

session = HTMLSession()
from bs4 import BeautifulSoup


def amazon_get_price_by_url(url):
    r = session.get(url)
    html = r.text
    soup = BeautifulSoup(html, "html.parser")
    tag = soup.find("span", id="price")
    return tag.text


# EXAMPLE
print(amazon_get_price_by_url(
    "https://www.amazon.co.uk//Bible-Large-Print-Harper-Bibles/dp/0061244899/ref=sr_1_1?crid=3GDWA4FIE0OKM&keywords=isbn%3A+0061244899&qid=1646754105&sprefix=isbn+0061244899%2Caps%2C74&sr=8-1#customerReviews"))

quit()
