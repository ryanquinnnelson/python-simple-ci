from bs4 import BeautifulSoup


def printSoup():
    soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
    print(soup.prettify())
